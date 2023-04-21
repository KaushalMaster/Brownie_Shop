from django.contrib import admin
from .models import Products, Product_details, registerOrders
# Register your models here.
admin.site.register(Products)
admin.site.register(Product_details)
admin.site.register(registerOrders)
