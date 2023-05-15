from django.db import models

# Create your models here.

class Proveedor(models.Model):
    """
    Modelo que representa a un proveedor en el sistema.

    Campos:
    - nombre (CharField): Nombre del proveedor.
    - apellido (CharField): Apellido del proveedor.
    - dni (IntegerField): Número de documento de identidad del proveedor.

    """
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    dni = models.IntegerField()
    
    def __str__(self) -> str:
        return f"{self.nombre} {self.apellido}"

class Producto(models.Model):
    """
    Modelo que representa un producto en el sistema.

    Campos:
        nombre (CharField): El nombre del producto.
        precio (FloatField): El precio del producto.
        stock_actual (IntegerField): La cantidad actual en stock del producto.
        proveedor (Proveedor): El proveedor del producto (clave foránea).

    """
    nombre = models.CharField(max_length=50)
    precio = models.FloatField(default=0)
    stock_actual = models.IntegerField()
    proveedor = models.ForeignKey(
        Proveedor,
        related_name="productos",
        on_delete=models.CASCADE,
    )
    
    def __str__(self) -> str:
        return self.nombre