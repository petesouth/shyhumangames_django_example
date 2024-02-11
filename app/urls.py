
from django.urls import path
from . import views



urlpatterns = [
    path('v2/suppliers/', views.SupplierListView.as_view(), name='supplier-list'),
]

