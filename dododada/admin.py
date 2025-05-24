from django.contrib import admin
from .models import Category, Product, Order, PointCharge

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'price', 'stock', 'created_at']
    list_filter = ['category', 'created_at']
    search_fields = ['name', 'description']
    readonly_fields = ['created_at', 'updated_at']

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['user', 'product', 'price_at_purchase', 'created_at']
    list_filter = ['created_at', 'user']
    search_fields = ['user__username', 'product__name']
    readonly_fields = ['created_at']

@admin.register(PointCharge)
class PointChargeAdmin(admin.ModelAdmin):
    list_display = ['user', 'amount', 'created_at']
    list_filter = ['created_at', 'user']
    search_fields = ['user__username']
    readonly_fields = ['created_at']