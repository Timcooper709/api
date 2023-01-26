from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models import Sum


# Create your models here.
class User(AbstractUser):
    
    # add additional fields in here

    def __str__(self):
        return self.username

class Category(models.Model):
    title     = models.CharField(max_length=50, null=True, blank=True)
    # foreginkey relates one model to another.
    # This is why I see the category title in admin instead of the pk.
    def __str__(self):
        return self.title       

class Item(models.Model):
    product          = models.CharField(max_length=300, null=True, blank=True)      
    manufacturer     = models.CharField(max_length=300, null=True, blank=True)
    date_received    = models.DateTimeField(auto_now_add=True)
    amount           = models.IntegerField(null=True, blank=True)
    item_description = models.TextField(null=True, blank=True)
     # foreginkey relates one model to another.
    category         = models.ForeignKey('Category', related_name='items', on_delete=models.CASCADE, null=True,blank=True) 
    # This is why I see the Item product in admin. If not there PK would show.
    def __str__ (self):
        return self.product
    @property
    def actual(self):
        x = self.amount - self.shipments.aggregate(Sum('quantity_shipped')).get('quantity_shipped__sum')
        return x

 
    
    


class Shipment(models.Model):
    attn             = models.CharField(max_length=200, null=True, blank=True)
    address_line_one = models.CharField(max_length=200, null=True, blank=True)
    address_line_two = models.CharField(max_length=200, null=True, blank=True)
    quantity_shipped = models.IntegerField(null=True, blank=True)   
    tracking_number  = models.CharField(max_length=50, null=True, blank=True) 
     # foreginkey relates one model to another.
    item             = models.ForeignKey('Item', related_name='shipments', on_delete=models.CASCADE, null=True,blank=True) 
    date             = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    
    def __str__(self):
        # This is an f string 
        return f"{self.quantity_shipped} {self.item} was shipped {self.date}"  









