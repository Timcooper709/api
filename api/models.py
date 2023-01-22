from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    
    # add additional fields in here

    def __str__(self):
        return self.username

class Aisle(models.Model):
    title            = models.CharField(max_length=10, null=True, blank=True)

    def __str__(self):  
        return self.title  

class Category(models.Model):
    title     = models.CharField(max_length=50, null=True, blank=True)
    aisle     = models.ForeignKey('Aisle', related_name='categories', on_delete=models.CASCADE, null=True,blank=True)


    def __str__(self):
        return self.title        


class Item(models.Model):
    product          = models.CharField(max_length=300, null=True, blank=True)      
    manufacturer     = models.CharField(max_length=300, null=True, blank=True)
    date_received    = models.DateTimeField(auto_now_add=True)
    total_quantity   = models.IntegerField(null=True, blank=True)
    item_description = models.TextField(null=True, blank=True)

    def __str__ (self):
        return self.product




