from django.contrib import admin
from .models import Seller, Customer, Product, Order


@admin.register(Seller)
class SellerAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone', 'description', 'address', 'password', 'category', 'subcategory']


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['customer_id', 'name', 'email', 'phone', 'address']


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['orderid', 'invoice']


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['product_id', 'name', 'description', 'category', 'subcategory', 'season', 'seller_id', 'image']
