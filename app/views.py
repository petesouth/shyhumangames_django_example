from rest_framework import generics, response
from rest_framework.pagination import CursorPagination
from .models import Supplier
from .serializers import SupplierSerializer
from django.http import JsonResponse

class SupplierPagination(CursorPagination):
    ordering = '-popularity'
    page_size = 10  # Adjust as needed
    cursor_query_param = 'cursor'
    cursor_page_query_param = 'cursor'


class SupplierListView(generics.ListAPIView):
    serializer_class = SupplierSerializer
    pagination_class = SupplierPagination
    queryset = Supplier.objects.all()  # Add this line

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        # Get the cursor value from request query parameters
        cursor = self.request.query_params.get(self.pagination_class.cursor_query_param)

        # Apply cursor-based pagination
        paginator = self.pagination_class()
        paginated_queryset = paginator.paginate_queryset(queryset, request)

        # Serialize the paginated data
        serializer = self.get_serializer(paginated_queryset, many=True)

        # Construct the response data with next and previous links
        response_data = {
            "next": paginator.get_next_link(),
            "previous": paginator.get_previous_link(),
            "results": serializer.data
        }

        # Return JSON response
        return JsonResponse(response_data)
