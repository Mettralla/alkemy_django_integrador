from django import forms
from .models import Producto, Proveedor

class ProveedorForm(forms.ModelForm):
    class Meta:
        model = Proveedor
        fields = ["nombre", "apellido", "dni"]