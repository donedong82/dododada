from django.db import models
from django.conf import settings
from django.utils import timezone

class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='카테고리명')
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = '카테고리'
        verbose_name_plural = '카테고리 목록'

class Product(models.Model):
    name = models.CharField(max_length=200, verbose_name='상품명')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products', verbose_name='카테고리')
    price = models.PositiveIntegerField(verbose_name='가격')
    stock = models.PositiveIntegerField(verbose_name='재고')
    description = models.TextField(verbose_name='상품 설명')
    image = models.ImageField(upload_to='products/', verbose_name='상품 이미지')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='등록일')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='수정일')
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = '상품'
        verbose_name_plural = '상품 목록'
        ordering = ['-created_at']

class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='orders', verbose_name='사용자')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='orders', verbose_name='상품')
    price_at_purchase = models.PositiveIntegerField(verbose_name='구매 시 가격')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='구매일')
    
    def __str__(self):
        return f"{self.user.username}의 {self.product.name} 주문"
    
    class Meta:
        verbose_name = '주문'
        verbose_name_plural = '주문 목록'
        ordering = ['-created_at']

class PointCharge(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='point_charges', verbose_name='사용자')
    amount = models.PositiveIntegerField(verbose_name='충전 금액')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='충전일')
    
    def __str__(self):
        return f"{self.user.username}의 {self.amount} 포인트 충전"
    
    class Meta:
        verbose_name = '포인트 충전'
        verbose_name_plural = '포인트 충전 목록'
        ordering = ['-created_at']