from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import get_object_or_404, ListCreateAPIView, ListAPIView
from .models import Item, Category, Shipment
from .serializers import ItemSerializer, ItemListSerializer, CategorySerializer, ShipmentListSerializer
from rest_framework.decorators import action
# Create your views here.


class ItemViewSet(ModelViewSet):
    queryset         = Item.objects.all()
    serializer_class = ItemSerializer

    def get_queryset(self):
        search_term = self.request.query_params.get("search")
        if search_term is not None:
            results = Item.objects.filter(product__icontains=self.request.query_params.get("search"))
        return results    
   
# When you make a request for a list of items the ItemListSerializer is called.
    def get_serializer_class(self):
        if self.action in ['list']:
            return ItemListSerializer
        return super().get_serializer_class()

       
   

class ItemListCreateView(ListCreateAPIView):
    serializer_class = ItemSerializer
   
    def get_queryset(self):
        return Item.objects.filter(category_id=self.kwargs["category_pk"])

    def perform_create(self, serializer, **kwargs):
        category = get_object_or_404(Category, pk=self.kwargs["category_pk"])
        serializer.save(category=category)        

class CategoryViewSet(ModelViewSet):
    queryset         = Category.objects.all()
    serializer_class = CategorySerializer

    def get_queryset(self):
        search_term = self.request.query_params.get("search")
        if search_term is not None:
            results = Category.objects.filter(title__icontains=self.request.query_params.get("search"))
        return results    

class ShipmentListCreateView(ListCreateAPIView):
    serializer_class = ShipmentListSerializer
   
    def get_queryset(self):
        return Shipment.objects.filter(item_id=self.kwargs["item_pk"])

    def perform_create(self, serializer, **kwargs):
        item = get_object_or_404(Item, pk=self.kwargs["item_pk"])
        serializer.save(item=item)

class ShipmentListView(ListAPIView):
    queryset = Shipment.objects.all()
    serializer_class = ShipmentListSerializer
#this is to override the get queryset to order the shipments in this list by the most recent
    def get_queryset(self):
        results=self.queryset.all()
        return results.order_by('-date')

class LowStockListView(ListAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemListSerializer 

    def get_queryset(self):
        return Item.objects.filter(amount__lt=100)   

