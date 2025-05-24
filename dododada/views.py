from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from .models import Category, Product, Order, PointCharge
from django.http import JsonResponse
import datetime

def test(request):
    pass

@login_required
def charge(request):
    """포인트 충전 페이지"""
    if request.method == 'POST':
        amount = request.POST.get('amount')
        if amount:
            amount = int(amount)
            PointCharge.objects.create(user=request.user, amount=amount)
            
            request.user.point += amount
            request.user.save()
            
            messages.success(request, f'{amount} 포인트가 성공적으로 충전되었습니다.')
        
    return render(request, 'dododada/charge.html')

@login_required
def products(request):
    """상품 목록 페이지"""
    categories = Category.objects.all()
    selected_category = request.GET.get('category', '')
    sort_option = request.GET.get('sort', '')
    
    products = Product.objects.all()
    
    if selected_category and selected_category != 'all':
        products = products.filter(category__name=selected_category)
    
    if sort_option == 'price_low':
        products = products.order_by('price')
    elif sort_option == 'price_high':
        products = products.order_by('-price')
    else:
        products = products.order_by('-created_at')
    
    context = {
        'products': products,
        'categories': categories,
        'selected_category': selected_category,
        'sort_option': sort_option
    }
    
    return render(request, 'dododada/products.html', context)

@login_required
def product_detail(request, product_id):
    """상품 상세 페이지"""
    product = get_object_or_404(Product, id=product_id)
    
    context = {
        'product': product
    }
    
    return render(request, 'dododada/product_detail.html', context)

@login_required
def purchase(request, product_id):
    """상품 구매 처리"""
    if request.method == 'POST':
        product = get_object_or_404(Product, id=product_id)
        
        if product.stock <= 0:
            messages.error(request, '상품의 재고가 부족합니다.')
            return redirect('dododada:product_detail', product_id=product.id)
        
        if request.user.point < product.price:
            messages.error(request, '포인트가 부족합니다.')
            return redirect('dododada:product_detail', product_id=product.id)
        
        try:
            Order.objects.create(
                user=request.user,
                product=product,
                price_at_purchase=product.price
            )
            
            request.user.point -= product.price
            request.user.save()
            
            product.stock -= 1
            product.save()
            
            # 구매자 및 구매 정보 출력
            purchase_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            print(f"[구매 정보] 사용자: {request.user.username}, 상품: {product.name}, 가격: {product.price}, 시간: {purchase_time}")
            
            messages.success(request, '상품이 성공적으로 구매되었습니다.')
            return redirect('dododada:orders')
            
        except Exception as e:
            messages.error(request, f'구매 처리 중 오류가 발생했습니다: {str(e)}')
            return redirect('dododada:product_detail', product_id=product.id)
    
    return redirect('dododada:product_detail', product_id=product_id)

@login_required
def orders(request):
    """주문 내역 페이지"""
    orders = Order.objects.filter(user=request.user).order_by('-created_at')
    
    context = {
        'orders': orders
    }
    
    return render(request, 'dododada/orders.html', context)