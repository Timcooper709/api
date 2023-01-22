from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import get_object_or_404
from .models import Item, Category
from .serializers import ItemSerializer, ItemListSerializer
# Create your views here.


class ItemViewSet(ModelViewSet):
    queryset         = Item.objects.all()
    serializer_class = ItemSerializer
   
    # This is where we are changing the perform / create function within this API view 
    # def perform_create(self, serializer, **kwargs):
        
    #     category = get_object_or_404(Category,pk=self.kwargs["category_pk"])
    #     serializer.save(category=category)

# When you make a request for a list of items the ItemListSerializer is called.
    def get_serializer_class(self):
        if self.action in ['list']:
            return ItemListSerializer
        return super().get_serializer_class()



