from django.shortcuts import render
from rest_framework import generics
from .models import Productos
from .serializers import ProductosSerializer,ProductosDetailSerializer


class ProductosListView(generics.ListAPIView): #Solo muestra el Listado de productos
    queryset = Productos.objects.all()
    serializer_class = ProductosSerializer


class ProductoDetailView(generics.RetrieveAPIView):
    lookup_field = "id"
    queryset = Productos.objects.all()
    serializer_class = ProductosDetailSerializer


#RESFULL  = model.modelviewset
#LISTAR = ListAPIView
#CREAR  = CreateAPIView
#ELIMINAR =DestroyAPIView
#ACTUALIZAR =UpdateAPIView
#LISTAR/CREAR = ListCreateAPIView
#RetrieveAPIView = para enlistar un solo modelo

