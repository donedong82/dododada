from django.urls import path
from .views import *

app_name = 'dododada'

urlpatterns = [
    path('test/', test, name='test'),
    path('charge/', charge, name='charge'),
    path('products/', products, name='products'),
    path('products/<int:product_id>/', product_detail, name='product_detail'),
    path('products/<int:product_id>/purchase/', purchase, name='purchase'),
    path('orders/', orders, name='orders'),
]