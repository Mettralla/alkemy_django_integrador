from django.shortcuts import render, redirect
from compra.models import Producto, Proveedor
from .forms import ProveedorForm, ProductoForm

# Create your views here.
def index(request):
    return render(request, 'index.html')

def new_proveedor(request):
    if request.method == 'POST':
        form = ProveedorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('productos')
    else:
        form = ProveedorForm()
    return render(request, 'new_proveedor.html', {'form': form})

def new_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('productos')
    else:
        form = ProductoForm()
    return render(request, 'new_producto.html', {'form': form})