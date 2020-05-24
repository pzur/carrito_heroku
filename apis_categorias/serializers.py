from rest_framework import serializers
from .models import Categoria
from apis_productos.models import Productos, Producto_Fotos, Producto_Precios


class PreciosProductosSerializer(serializers.ModelSerializer):  # Los Campos Hijos
    class Meta:
        model = Producto_Precios
        fields = ['precioventa', 'precioinsumo', 'precioespecial']


class FotosProductosSerializer(serializers.ModelSerializer):  # Los Campos Hijos
    class Meta:
        model = Producto_Fotos
        fields = ['foto1', 'foto2', 'foto3', 'foto4']


class ProductosSerializer(serializers.HyperlinkedModelSerializer):
    lista_precios = PreciosProductosSerializer(many=True, read_only=True)  # Padre
    producto_fotos = FotosProductosSerializer(many=True, read_only=True)  # Padre

    class Meta:
        model = Productos  # Hijo
        fields = ['id', 'producto', 'caracteristicas', 'lista_precios', 'producto_fotos']


# Serializers define the API representation.
class CategoriaSerializer(serializers.HyperlinkedModelSerializer):
    productos = ProductosSerializer(many=True, read_only=True)  # Abuelo

    class Meta:
        model = Categoria
        fields = ('id', 'nombre', 'descripcion', 'productos')
