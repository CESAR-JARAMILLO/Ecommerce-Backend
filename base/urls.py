from importlib.resources import path
from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [
  path('', views.getRoutes, name='routes'),
  path('products/', views.getProducts, name='products'),
  path('products/<str:pk>/', views.getProduct, name='product'),
]