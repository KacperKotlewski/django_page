from django.db import models
from product.models import Product
from phone_field import PhoneField

# Create your models here.

class Orders(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, blank=True, null=True)
    count = models.IntegerField()
    name = models.CharField(max_length=64)
    surname = models.CharField(max_length=64)
    email = models.EmailField(max_length=254, unique=True)
    phone = models.CharField(max_length=12)
    adress = models.CharField(max_length=120, blank=True, null=True)
    house_number = models.CharField(max_length=12, blank=True, null=True)
    zip_code = models.CharField(max_length=6, blank=True, null=True)
    city_name = models.CharField(max_length=120, blank=True, null=True)
    is_confirmed = models.BooleanField(default=False)

    def __str__(self):
        return str(self.name) + " " + str(self.surname) 