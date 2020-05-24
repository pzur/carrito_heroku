from rest_framework import serializers
from .models import Productos, Producto_Precios, Producto_Fotos



class PreciosProductosSerializer(serializers.ModelSerializer):  # Los Campos Hijos
    class Meta:
        model = Producto_Precios
        fields = ['precioventa', 'precioinsumo', 'precioespecial']


class FotosProductosSerializer(serializers.ModelSerializer):  # Los Campos Hijos
    class Meta:
        model = Producto_Fotos
        fields = ['foto1', 'foto2', 'foto3', 'foto4']


# Serializers define the API representation.
class ProductosSerializer(serializers.HyperlinkedModelSerializer):
    lista_precios = PreciosProductosSerializer(many=True, read_only=True) #Hijo1
    producto_fotos = FotosProductosSerializer(many=True, read_only=True)  #Hijo2

    class Meta:
        model = Productos # padre
        fields = ['id', 'producto', 'caracteristicas', 'lista_precios', 'producto_fotos']



class ProductosDetailSerializer(serializers.HyperlinkedModelSerializer):
    lista_precios = PreciosProductosSerializer(many=True, read_only=True) #HIJO1
    producto_fotos = FotosProductosSerializer(many=True, read_only=True)  #HIJO2


    class Meta:
        model = Productos #PADRE
        fields = ['id', 'producto', 'caracteristicas', 'descripcion', 'categoria','lista_precios', 'producto_fotos']



# https://www.django-rest-framework.org/api-guide/generic-views/
