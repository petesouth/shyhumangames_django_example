from datetime import timedelta
import os
import uuid
from django.db.models import Q
from django.utils import timezone
from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Supplier, KeyValueJsonStoreTTL
from .serializers import SupplierSerializer, KeyValueJsonStoreSerializer
from django.http import JsonResponse
from rest_framework.pagination import CursorPagination



class KeyValueJsonStoreAPIView(APIView):
    def get(self, request, *args, **kwargs):
        try:
            keys = request.query_params.get('keys', '').strip()
            if keys:
                keys = keys.split(',')
                values = KeyValueJsonStoreTTL.objects.filter(key__in=keys, expires_at__gt=timezone.now())
            else:
                return Response({"error": "No keys provided or keys are empty."}, status=status.HTTP_400_BAD_REQUEST)

            # Reset TTL for matched records
            for value in values:
                value.expires_at = timezone.now() + timedelta(minutes=5)
                value.save()

            serializer = KeyValueJsonStoreSerializer(values, many=True)
            return Response(serializer.data)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def post(self, request, *args, **kwargs):
        try:
            value = request.data.get('value')
            if not value:
                return Response({"error": "Value field is required."}, status=status.HTTP_400_BAD_REQUEST)

            unique_key = str(uuid.uuid4())

            ttl_minutes = int(os.environ.get('TTL_MINUTES', 5))  # Use default of 5 minutes if not specified

            new_entry = KeyValueJsonStoreTTL.objects.create(
                key=unique_key,
                value=value,
                expires_at=timezone.now() + timedelta(minutes=ttl_minutes)
            )

            serializer = KeyValueJsonStoreSerializer(new_entry)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)



    def patch(self, request, *args, **kwargs):
        try:
            if not request.data:
                return Response({"error": "Patch data is required."}, status=status.HTTP_400_BAD_REQUEST)

            responses = []
            for key, value in request.data.items():
                obj, created = KeyValueJsonStoreTTL.objects.update_or_create(
                    key=key,
                    defaults={'value': value, 'expires_at': timezone.now() + timedelta(minutes=5)}
                )
                serializer = KeyValueJsonStoreSerializer(obj)
                responses.append(serializer.data)

            return Response(responses, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        

class SupplierPagination(CursorPagination):
    ordering = '-id'
    page_size = 20  # Adjust as needed
    cursor_query_param = 'cursor'
    cursor_page_query_param = 'cursor'

class SupplierListView(generics.ListAPIView):
    serializer_class = SupplierSerializer
    pagination_class = SupplierPagination

    def get_queryset(self):
        queryset = Supplier.objects.all()
        city = self.request.query_params.get('city', None)
        search = self.request.query_params.get('search', None)

        if city and city.isdigit():
            queryset = queryset.filter(city=city)
        if search:
            queryset = queryset.filter(Q(name__icontains=search) | Q(name_en__icontains=search))

        return queryset

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        paginator = self.pagination_class()
        paginated_queryset = paginator.paginate_queryset(queryset, request)
        serializer = self.get_serializer(paginated_queryset, many=True)

        response_data = {
            "next": paginator.get_next_link(),
            "previous": paginator.get_previous_link(),
            "results": serializer.data
        }

        response = JsonResponse(response_data)
        
        return response
