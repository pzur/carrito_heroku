from django.db import models
from apis_categorias.models import Categoria
from django.contrib.auth.models import User

class Productos(models.Model):
    producto = models.CharField(max_length=120)
    descripcion = models.TextField(blank=True, null=True)
    caracteristicas = models.CharField(max_length=20, blank=True, null=True)
    estado = models.BooleanField(default=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, blank=True, null=True, related_name='productos')
    #proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE, blank=True, null=True)
    fecha_creacion = models.DateTimeField(blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True,related_name="productosuser")

    def __str__(self):
        return self.producto


class Ingredientes(models.Model):
    producto = models.ForeignKey(Productos, on_delete=models.CASCADE, related_name="ingredientes")
    proteina = models.FloatField()
    carbohidrato = models.FloatField()

    def __str__(self):
        return self.producto.producto

class Producto_Fotos(models.Model):
    photo = models.ImageField(upload_to='Productos/Fotos', null=True, blank=True)
    photo = models.ImageField(upload_to='Productos/Fotos', null=True, blank=True)
    photo = models.ImageField(upload_to='Productos/Fotos', null=True, blank=True)
    photo = models.ImageField(upload_to='Productos/Fotos', null=True, blank=True)
    producto = models.ForeignKey(Productos, on_delete=models.CASCADE, related_name='producto_fotos')
    estado = models.BooleanField(default=True)

    def __str__(self):
        return str(self.producto.producto)


class Producto_Precios(models.Model):
    precioinsumo = models.DecimalField(max_digits=5, decimal_places=2)
    precioventa = models.DecimalField(max_digits=5, decimal_places=2)
    precioespecial = models.DecimalField(max_digits=5, decimal_places=2)
    productos = models.ForeignKey(Productos, on_delete=models.CASCADE,related_name='lista_precios')
    estado = models.BooleanField(default=True)

    def __str__(self):
        return self.productos.producto + ' Precio de Venta:' + str(self.precioventa) + ' Precio Especial:' + str(
            self.precioespecial)
