from django.urls import path
from . import views

urlpatterns = [
    path('productos/listado', views.index, name='productos'),
    path('proveedor/nuevo/', views.new_proveedor, name='nuevo_proveedor'),
    path('producto/nuevo/', views.new_producto, name='nuevo_producto'),
    path('proveedores/listado', views.proveedor_list, name='proveedores')
    
]
