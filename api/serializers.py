from rest_framework import serializers 
from .models import Item


class ItemSerializer(serializers.ModelSerializer):


    class Meta:
        model = Item
        fields = ['pk', 'product', 'manufacturer', 'date_received', 'total_quantity', 'item_description', 'category']
        