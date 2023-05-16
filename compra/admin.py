from django.contrib import admin
from .models import Producto, Proveedor

# Register your models here.

class ProductoAdmin(admin.ModelAdmin):
    list_display = ("id", "nombre", "precio", "stock_actual", "proveedor")

class ProveedorAdmin(admin.ModelAdmin):
    list_display = ("id", "nombre", "apellido", "dni")

admin.site.register(Proveedor, ProveedorAdmin)
admin.site.register(Producto, ProductoAdmin)