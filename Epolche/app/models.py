from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True, blank=False)
    name = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=10, null=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=255, null=True)
    description = models.TextField()
    price = models.FloatField()
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='products/')

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=255, null=True)
    description = models.TextField()
    
    def __str__(self):
        return self.name

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=False)
    date_order = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=False, null=True, blank=False)
    total_price = models.FloatField()
    transaction_id = models.CharField(max_length=255, null=True)

    def __str__(self):
        return str(self.id)

    
class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True, blank=False)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, blank=False)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    date_add = models.DateTimeField(auto_now_add=True)

class ShippingAddress(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=False)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True, blank=False)
    address = models.CharField(max_length=255, null=True)
    city = models.CharField(max_length=255, null=True)
    state = models.CharField(max_length=255, null=True)
    date_added = models.CharField(max_length=255, null=True)
    
    def __str__(self):
        return str(self.address)