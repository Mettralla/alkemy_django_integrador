from django.urls import path
from . import views

urlpatterns = [
    path('productos/', views.index, name='productos'),
    path('crear_proveedor/', views.create_proveedor, name='crear_proveedor')
]
