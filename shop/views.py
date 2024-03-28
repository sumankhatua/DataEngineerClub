from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def shop_home(request):
    return render(request, 'shop/shop_home.html')

def shop_about(request):
    return render(request, 'shop/shop_about.html')

def shop_contact(request):
    return render(request, 'shop/shop_contact.html')

def shop_tracker(request):
    return render(request, 'shop/shop_tracker.html')

def shop_search(request):
    return render(request, 'shop/shop_search.html')

def shop_product_view(request):
    return render(request, 'shop/shop_product_view.html')

def shop_checkout(request):
    return render(request, 'shop/shop_checkout.html')

