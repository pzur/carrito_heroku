from django.contrib import admin
from .models import *

admin.site.register(Categoria)
admin.site.register(Productos)
admin.site.register(Proveedor)
admin.site.register(Producto_Fotos)
admin.site.register(Producto_Precios)
admin.site.register(Personas)
admin.site.register(Tarjetas)
admin.site.register(TipoDocumento)
admin.site.register(Promociones)
admin.site.register(Promocion_Detalles)
admin.site.register(Pedidos)
admin.site.register(Pedidos_Detalles)
admin.site.register(Pagos)
admin.site.register(Despachos)
admin.site.register(Detalle_Despacho)
admin.site.register(Devoluciones)
admin.site.register(CarritoSession)
admin.site.register(CarritoDetalleSession)
admin.site.register(Comentarios)
admin.site.register(Ingredientes)

# Register your models here.
