from django.shortcuts import render, get_object_or_404
from .models import Product, Order
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse

def product_list(request):
    products = Product.objects.all()
    return render(request, 'products/product_list.html', {'products': products})

def product_detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    return render(request, 'products/product_detail.html', {'product': product})
from django.http import JsonResponse

@login_required
def create_order(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        quantity = int(request.POST['quantity'])
        total_price = product.price * quantity
        order = Order.objects.create(
            user=request.user,
            product=product,
            quantity=quantity,
            total_price=total_price
        )
        return JsonResponse({'status': 'success', 'order_id': order.id})
    return JsonResponse({'status': 'error', 'message': 'Invalid request'}, status=400)

@login_required
def user_orders(request):
        orders = Order.objects.filter(user=request.user)
        return render(request, 'products/user_orders.html', {'orders': orders})


def search(request):
    query = request.GET.get('query')
    results = []
    if query:
        results = Product.objects.filter(name__icontains=query)
    return render(request, 'products/products_search.html', {'results': results, 'query': query})

