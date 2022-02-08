from django.urls import path
from . import views

app_name='cart'

urlpatterns = [
    
    # access path: 127.0.0.1:8000/cart/add/<int:product_id>/
	path('add/<int:product_id>/', views.add_cart, name='add_cart'), 
 
    # access path: 127.0.0.1:8000/cart/cart_detail
	path('', views.cart_detail, name='cart_detail'),
 
    # access path: 127.0.0.1:8000/cart/remove/<int:product_id>/
	path('remove/<int:product_id>/', views.cart_remove, name='cart_remove'), # valid after course 18
	
     # access path: 127.0.0.1:8000/cart/full_remove/<int:product_id>/
 	path('full_remove/<int:product_id>/', views.full_remove, name='full_remove'), #valid after course 18
  
    # access path: 127.0.0.1:8000/cart/cart_detail_cash
 	path('cart/cart_detail_cash/', views.cart_detail_cash, name='cart_detail_cash'),


]