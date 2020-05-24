from django.shortcuts import render
from .models import *
from django.http import Http404, response
from django.db import connection
from rest_framework import viewsets, decorators, parsers, status
from .Serializers import *




# Vista Basada en Funciones QUERYSETS
def all_productos(request):
    all_productos = Productos.objects.all()
    context = {'productos': all_productos}
    return render(request, 'productos.html', context)


def detail_productos(request, id):
    try:
        productos_id = Productos.objects.get(pk=id)
        context = {'producto_id': productos_id}
    except Productos.DoesNotExist:
        raise Http404("producto no registado en el carrito - ???????")
    return render(request, 'productodetail.html', context)


def filtar_productos(request, nombre):
    try:
        busqueda = Productos.objects.filter(producto__contains=nombre)
        context = {'productos': busqueda}
    except Productos.DoesNotExist:
        raise Http404("producto no registado en el carrito - ???????")
    return render(request, 'productos.html', context)


def productos_fotos(request):
    all_platos = Producto_Fotos.objects.all()
    context = {'productos': all_platos}
    return render(request, 'productosfotos.html', context)


def productosycategorias(request):
    try:
        join = Productos.objects.select_related("categoria")
        context = {'productos': join}
    except Productos.DoesNotExist:
        raise Http404("productos no registado en el carrito - ???????")
    return render(request, 'productos.html', context)


# MYSQL DIRECTAMENTE

def all_platos_sql(request):
    with connection.cursor() as cursor:
        cursor.execute("select * from usuarios_producto")
        rowdata = cursor.fetchall()
        resul = []
        for item in rowdata:
            resul.append(list(item))
        context = {'productos': resul}
    return render(request, 'productossql.html', context)


def all_platos_sql_procedure(request):
    with connection.cursor() as cursor:
        cursor.callproc("usp_productos")
        rowdata = cursor.fetchall()
        resul = []
        for item in rowdata:
            resul.append(list(item))
        context = {'productos': resul}
    return render(request, 'productossql.html', context)


def all_platos_categoria(request, idcat):
    with connection.cursor() as cursor:
        cursor.callproc("usp_busprod_cat", [idcat])
        rowdata = cursor.fetchall()
        resul = []
        for item in rowdata:
            resul.append(list(item))
        context = {'productos': resul}
    return render(request, 'productossql.html', context)


#    MODELO  -- VISTA  -- TEMPLATE
#              RUTA=URL

# Django Rest Framework
# ===============================

class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer


class ProductosingredientesViewSet(viewsets.ModelViewSet):
    queryset = Productos.objects.all()
    serializer_class = ProductosSerializer


class CategoriasproductossViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriasproductosSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


#Para El perfil de la Persona

class PersonaViewSet(viewsets.ModelViewSet):
    serializer_class = PersonaSerializer
    queryset = Personas.objects.all()

    @decorators.action(
        detail=True,
        methods=['PUT'],
        serializer_class=PersonaFotoSerializer,
        parser_classes=[parsers.MultiPartParser],
    )
    def pic(self, request, pk):
        obj = self.get_object()
        serializer = self.serializer_class(obj, data=request.data,
                                           partial=True)
        if serializer.is_valid():
            serializer.save()
            return response.Response(serializer.data)
        return response.Response(serializer.errors,
                                 status.HTTP_400_BAD_REQUEST)
