from django.db.models import Q
from rest_framework import generics
from .models import Supplier
from .serializers import SupplierSerializer
from django.http import JsonResponse
from rest_framework.pagination import CursorPagination

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
