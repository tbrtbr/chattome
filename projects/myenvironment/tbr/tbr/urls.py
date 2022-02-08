"""tbr URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include


# for importing the shop views
from shop import views

# for mapping the static and medis url
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index, name='index'), # for 127.0.0.1:8000 page
    path('shop/', include('shop.urls')), # add shop app path
    path('search/', include('search_app.urls')), # add search app path   
    path('cart/', include('cart.urls')), # add cart app path   
    path('order/', include('order.urls')), # add order app path
    path('account/create/', views.signupView, name='signup'), # add signup path
    path('account/login/', views.signinView, name='signin'), # add signin path
    path('account/logout/', views.signoutView, name='signout'), # add signout path  
        
]






# for mapping the static and medis url
if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
	urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)