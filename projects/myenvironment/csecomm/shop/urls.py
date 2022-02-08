from django.urls import path
from . import views

app_name='shop'

urlpatterns = [
	path('', views.allProdCat, name='allProdCat'), # the name is for the url, not for the view; map all the products without a category
	path('<slug:c_slug>/', views.allProdCat, name='products_by_category'), # c_slug refer to views.py in shop app, def allProCat; map all the products by category
	path('<slug:c_slug>/<slug:product_slug>/', views.ProdCatDetail, name='ProdCatDetail'),
]