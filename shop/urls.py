from django.urls import path
from . import views

urlpatterns = [
    path('', views.shop_home, name='ShopHome'),
    path('about/', views.shop_about, name='ShopAbout'),
    path('contact', views.shop_contact, name='ShopContactUs'),
    path('tracker/', views.shop_tracker, name='ShopTracker'),
    path('search/', views.shop_search, name='ShopSearch'),
    path('productview/', views.shop_product_view, name='ShopProductView'),
    path('checkout/', views.shop_checkout, name='ShopCheckout'),
]