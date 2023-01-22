from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    
    # add additional fields in here

    def __str__(self):
        return self.username

class Aisle(models.Model):
    title            = models.IntegerField(max_length=300, null=True, blank=True)

    def __str__(self):  
        return self.title  


class Item(models.Model):
    product          = models.CharField(max_length=300, null=True, blank=True)      
    manufacturer     = models.CharField(max_length=300, null=True, blank=True)
    date_received    = models.DateTimeField(auto_now_add=True)
    total_quantity   = models.IntegerField(max_length=300, null=True, blank=True)
    date_shipped     = models.DateTimeField(auto_now_add=True)
    item_description = models.TextField(null=True, blank=True)

    def __str__ (self):
        return self.product




