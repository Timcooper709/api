from django.contrib import admin
from .models import User, Aisle, Category, Item, Shipping
# Register your models here.


admin.site.register(User)
admin.site.register(Aisle)
admin.site.register(Category)
admin.site.register(Item)
admin.site.register(Shipping)
