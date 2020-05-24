from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User


# Serializers define the API representation.
class CategoriaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Categoria
        fields = ('nombre', 'descripcion')


class IngredienteSerializer(serializers.ModelSerializer):  # Los Campos Hijos
    class Meta:
        model = Ingredientes
        fields = "__all__"


class ProductosSerializer(serializers.ModelSerializer):  # El Padre
    ingredientes = IngredienteSerializer(many=True, read_only=True)  # La Relacion entre Hijo y Padre

    class Meta:
        model = Productos
        fields = ("producto", "descripcion", "ingredientes")


# Tendria qure crear los Nietos
# Los Nietos relacionarlos con los hijos   # Esto seria los nuevos Hijos


class Productos2Serializer(serializers.ModelSerializer):  # Hijos se puede convertir en padre
    class Meta:
        model = Productos
        fields = "__all__"


class CategoriasproductosSerializer(serializers.ModelSerializer):  # Padre se puede convertir en abuelo
    productos = Productos2Serializer(many=True, read_only=True)

    class Meta:
        model = Categoria
        fields = ("nombre", "productos",)


# Tomado de la documentacion de djangorestframework

class UserSerializer(serializers.ModelSerializer):  # es un servicio para un Crud
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff']


# Serializando el Usuario y Persona


class PersonaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Personas
        fields = ['telefono', 'ruc', 'foto']
        read_only_fields = ['foto']


class PersonaFotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Personas
        fields = ['foto']
