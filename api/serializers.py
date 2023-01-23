from rest_framework import serializers 
from .models import Item


class ItemSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(read_only=True,slug_field="title")

    class Meta:
        model = Item
        fields = ['pk', 'product', 'manufacturer', 'date_received', 'total_quantity', 'item_description', 'category']
        
class ItemListSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(read_only=True,slug_field="title")

    class Meta:
        model = Item
        fields = ['pk', 'product', 'total_quantity', 'category']       