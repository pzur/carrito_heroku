from django.db import models
from django.contrib.auth.models import User


class Categoria(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True, null=True)
    estado = models.BooleanField(default=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.nombre


class Proveedor(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=300, null=True, blank=True)
    correo = models.EmailField(blank=True, null=True)
    telefono = models.CharField(max_length=15, null=True, blank=True)
    web = models.CharField(max_length=300, null=True, blank=True)
    ruc = models.CharField(max_length=15, null=True, blank=True)
    estado = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre


class Productos(models.Model):
    producto = models.CharField(max_length=120)
    descripcion = models.TextField(blank=True, null=True)
    caracteristicas = models.CharField(max_length=20, blank=True, null=True)
    estado = models.BooleanField(default=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, blank=True, null=True, related_name='productos')
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE, blank=True, null=True)
    fecha_creacion = models.DateTimeField(blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.producto


class Ingredientes(models.Model):
    producto = models.ForeignKey(Productos, on_delete=models.CASCADE, related_name="ingredientes")
    proteina = models.FloatField()
    carbohidrato = models.FloatField()

    def __str__(self):
        return self.producto.producto


class Producto_Fotos(models.Model):
    foto1 = models.ImageField(upload_to='Productos/Fotos', null=True, blank=True)
    foto2 = models.ImageField(upload_to='Productos/Fotos', null=True, blank=True)
    foto3 = models.ImageField(upload_to='Productos/Fotos', null=True, blank=True)
    foto4 = models.ImageField(upload_to='Productos/Fotos', null=True, blank=True)
    producto = models.ForeignKey(Productos, on_delete=models.CASCADE, related_name='producto_fotos')
    estado = models.BooleanField(default=True)

    def __str__(self):
        return str(self.producto.producto)


class Producto_Precios(models.Model):
    precioinsumo = models.DecimalField(max_digits=5, decimal_places=2)
    precioventa = models.DecimalField(max_digits=5, decimal_places=2)
    precioespecial = models.DecimalField(max_digits=5, decimal_places=2)
    productos = models.ForeignKey(Productos, on_delete=models.CASCADE, related_name='producto_precios222')
    estado = models.BooleanField(default=True)

    def __str__(self):
        return self.productos.producto + ' Precio de Venta:' + str(self.precioventa) + ' Precio Especial:' + str(
            self.precioespecial)


class Personas(models.Model):
    # Clientes,Despachador,Administrador,Operador
    direccion = models.CharField(max_length=300, null=True, blank=True)
    correo = models.EmailField(blank=True, null=True)
    telefono = models.CharField(max_length=15, null=True, blank=True)
    ruc = models.CharField(max_length=15, null=True, blank=True)
    foto = models.ImageField(upload_to='Personas/Fotos', null=True, blank=True)
    estado = models.BooleanField(default=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='personas')
    estado = models.BooleanField(default=True)

    def __str__(self):
        return str(self.user.username)


class Tarjetas(models.Model):
    tarjetanombre = models.CharField(max_length=300, null=True, blank=True)
    tarjetanumero = models.CharField(max_length=30, null=True, blank=True)
    tarjetacvv = models.IntegerField(null=True, blank=True)
    tarjetaexp = models.DateField(null=True, blank=True)
    persona = models.ForeignKey(Personas, on_delete=models.CASCADE)
    estado = models.BooleanField(default=True)

    def __str__(self):
        return str(self.tarjetanombre)


class TipoDocumento(models.Model):
    documento_items = ((0, 'Boleta'), (1, 'Factura'), (2, 'Ticket'))
    nombre = models.IntegerField(choices=documento_items, default=0)
    descripcion = models.TextField(blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    estado = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre


class Promociones(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(null=True, blank=True)
    promociondesde = models.DateTimeField(null=True, blank=True)
    promocionhasta = models.DateTimeField(null=True, blank=True)
    estado = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre


class Promocion_Detalles(models.Model):
    promocion = models.ForeignKey(Promociones, on_delete=models.CASCADE)
    producto = models.ForeignKey(Productos, on_delete=models.CASCADE)
    estado = models.BooleanField(default=True)
    porcentajedescuento = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return str(self.id)


class Pedidos(models.Model):
    numeroped = models.IntegerField()
    pedidofecha = models.DateTimeField()
    completo = models.BooleanField(default=True)
    tipodocumento = models.ForeignKey(TipoDocumento, on_delete=models.CASCADE)
    numerodoc = models.IntegerField()
    cliente = models.ForeignKey(Personas, on_delete=models.CASCADE, related_name='cliente')
    promocion = models.ForeignKey(Promociones, on_delete=models.CASCADE, related_name='promociones')
    estado = models.BooleanField(default=True)

    def __str__(self):
        return str(self.numeroped)


class Pedidos_Detalles(models.Model):
    pedido = models.ForeignKey(Pedidos, on_delete=models.CASCADE)
    producto = models.ForeignKey(Productos, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    precioelegido = models.DecimalField(max_digits=5, decimal_places=2)
    descuento = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return str(self.id)


class Pagos(models.Model):
    pedido = models.ForeignKey(Pedidos, on_delete=models.CASCADE)
    tarjetanombre = models.CharField(max_length=300, null=True, blank=True)
    tarjetanumero = models.CharField(max_length=30, null=True, blank=True)
    subtotal = models.DecimalField(max_digits=5, decimal_places=2)
    igv = models.DecimalField(max_digits=5, decimal_places=2)
    descuento = models.DecimalField(max_digits=5, decimal_places=2)
    neto = models.DecimalField(max_digits=5, decimal_places=2)
    estado = models.BooleanField(default=True)

    def __str__(self):
        return str(self.id)


class Despachos(models.Model):
    pedido = models.ForeignKey(Pedidos, on_delete=models.CASCADE)
    despachador = models.ForeignKey(Personas, on_delete=models.CASCADE)
    observaciones = models.TextField(null=True, blank=True)
    # estas coordenadas se refieren al punto de partida
    cordenadamapa1 = models.IntegerField()
    cordenadamapa2 = models.IntegerField()
    fechahoradespacho = models.DateTimeField()
    estado = models.BooleanField(default=True)

    def __str__(self):
        return str(self.id)


class Detalle_Despacho(models.Model):
    despacho = models.ForeignKey(Despachos, on_delete=models.CASCADE)
    comentarios = models.TextField(null=True, blank=True)
    fechahoradespachoentrega = models.DateTimeField()
    # estas coordenadas se refieren cuando el despachador salio a realizar la entrega
    cordenadaubicacion1 = models.IntegerField()
    cordenadaubicacion2 = models.IntegerField()
    foto1 = models.ImageField(upload_to='Despachos/Fotos', null=True, blank=True)
    foto2 = models.ImageField(upload_to='Despachos/Fotos', null=True, blank=True)
    foto3 = models.ImageField(upload_to='Despachos/Fotos', null=True, blank=True)
    foto4 = models.ImageField(upload_to='Despachos/Fotos', null=True, blank=True)

    def __str__(self):
        return str(self.id)


class Devoluciones(models.Model):
    pedido = models.ForeignKey(Pedidos, on_delete=models.CASCADE)
    cliente = models.ForeignKey(Personas, on_delete=models.CASCADE)
    fechadevolucion = models.DateTimeField()
    motivo = models.TextField(null=True, blank=True)
    aprobado = models.BooleanField(default=True)

    def __str__(self):
        return str(self.id)


class CarritoSession(models.Model):
    cliente = models.ForeignKey(Personas, on_delete=models.CASCADE)
    pedidofecha = models.DateTimeField()
    promocion = models.ForeignKey(Promociones, on_delete=models.CASCADE)
    estado = models.BooleanField(default=True)

    def __str__(self):
        return str(self.id)


class CarritoDetalleSession(models.Model):
    carrito = models.ForeignKey(CarritoSession, on_delete=models.CASCADE)
    producto = models.ForeignKey(Productos, on_delete=models.CASCADE)
    precio = models.DecimalField(max_digits=5, decimal_places=2)
    cantidad = models.IntegerField()
    descuento = models.DecimalField(max_digits=5, decimal_places=2)
    igv = models.DecimalField(max_digits=5, decimal_places=2)
    subtotal = models.DecimalField(max_digits=5, decimal_places=2)
    total = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return str(self.id)


class Comentarios(models.Model):
    pedido = models.ForeignKey(Pedidos, on_delete=models.CASCADE)
    cliente = models.ForeignKey(Personas, on_delete=models.CASCADE, null=True, blank=True)
    comentarios = models.TextField(null=True, blank=True)
    estrellas = models.BooleanField(default=True)

    def __str__(self):
        return str(self.id)
