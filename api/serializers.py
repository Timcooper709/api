from rest_framework import serializers 
from .models import Item, Category, Shipment

class ShipmentListSerializer(serializers.ModelSerializer):
    item = serializers.SlugRelatedField(read_only=True,slug_field="product")

    class Meta:
        model = Shipment
        fields = ['pk', 'item', 'quantity_shipped', 'date', 'attn', 'address_line_one', 'address_line_two', 'tracking_number']  


class ItemSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(read_only=True,slug_field="title")
    shipments     = ShipmentListSerializer(many=True, read_only=True)
   

    class Meta:
        model = Item
        fields = ['pk', 'product', 'manufacturer', 'date_received', 'total_quantity', 'item_description', 'category', 'shipments']
        
class ItemListSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(read_only=True,slug_field="title")

    class Meta:
        model = Item
        fields = ['pk', 'product', 'total_quantity', 'category']   

class CategorySerializer(serializers.ModelSerializer):  
    items = ItemListSerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = ['pk', 'title', 'items']  

class ShipmentListSerializer(serializers.ModelSerializer):
    item = serializers.SlugRelatedField(read_only=True,slug_field="product")

    class Meta:
        model = Shipment
        fields = ['pk', 'item', 'quantity_shipped', 'date', 'attn', 'address_line_one', 'address_line_two', 'tracking_number']                     