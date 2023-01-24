from django.contrib import admin
from .models import User, Category, Item, Shipment
# Register your models here.


admin.site.register(User)
admin.site.register(Category)
admin.site.register(Item)
admin.site.register(Shipment)
