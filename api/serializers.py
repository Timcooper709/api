from rest_framework import serializers 
from .models import Item, Category, Shipment


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

class CategorySerializer(serializers.ModelSerializer):  
    items = serializers.SlugRelatedField(read_only=True,slug_field="product", many=True)

    class Meta:
        model = Category
        fields = ['pk', 'title', 'items']  

class ShipmentListSerializer(serializers.ModelSerializer):
    shipments = serializers.SlugRelatedField(read_only=True,slug_field="item")

    class Meta:
        model = Shipment
        fields = ['pk', 'item', 'quantity_shipped', 'tracking_number', 'sent_to', 'date']                     