
from django.urls import path
from . import views


urlpatterns = [
    path('v2/values/', views.KeyValueJsonStoreAPIView.as_view(), name='key-value-store'),
    path('v2/suppliers/', views.SupplierListView.as_view(), name='supplier-list'),
]

