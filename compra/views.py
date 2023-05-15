from django.shortcuts import render, redirect
from compra.models import Producto, Proveedor
from .forms import ProveedorForm

# Create your views here.
def index(request):
    return render(request, 'index.html')

def create_proveedor(request):
    if request.method == 'POST':
        form = ProveedorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('productos')
    else:
        form = ProveedorForm()
    return render(request, 'create_proveedor.html', {'form': form})