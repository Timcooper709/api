from django.contrib import admin
from .models import User, Aisle, Category
# Register your models here.


admin.site.register(User)
admin.site.register(Aisle)
admin.site.register(Category)
