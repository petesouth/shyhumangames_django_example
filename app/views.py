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
        keys = request.query_params.get('keys')
        if keys:
            keys = keys.split(',')
            values = KeyValueJsonStoreTTL.objects.filter(key__in=keys, expires_at__gt=timezone.now())
            # Reset TTL
            for value in values:
                value.expires_at = timezone.now() + timedelta(minutes=5)
                value.save()
        else:
            values = KeyValueJsonStoreTTL.objects.filter(expires_at__gt=timezone.now())
        serializer = KeyValueJsonStoreSerializer(values, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = KeyValueJsonStoreSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, *args, **kwargs):
        for key, value in request.data.items():
            obj, created = KeyValueJsonStoreTTL.objects.update_or_create(
                key=key,
                defaults={'value': value, 'expires_at': timezone.now() + timedelta(minutes=5)}
            )
        return Response({"message": "Updated successfully"}, status=status.HTTP_200_OK)







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
