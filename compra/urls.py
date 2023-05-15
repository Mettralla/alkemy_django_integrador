from django.urls import path
from . import views

urlpatterns = [
    path('productos/', views.index, name='productos'),
    path('nuevo_proveedor/', views.new_proveedor, name='nuevo_proveedor'),
    path('nuevo_producto/', views.new_producto, name='nuevo_producto')
    
]
