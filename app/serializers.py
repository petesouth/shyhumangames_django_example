from rest_framework import serializers
from .models import Supplier, KeyValueJsonStoreTTL

class KeyValueJsonStoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = KeyValueJsonStoreTTL
        fields = ['key', 'value', 'created_at', 'expires_at']


class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = '__all__'  # Include all fields from the Supplier model
