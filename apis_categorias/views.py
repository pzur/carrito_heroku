from django.shortcuts import render
from .models import *
from django.http import Http404, response
from django.db import connection
from rest_framework import viewsets, decorators, parsers, status
from .serializers import CategoriaSerializer
from rest_framework import generics
from rest_framework import serializers


# class CategoriaViewSet(generics.ListAPIView): # Rest Full
#    queryset = Categoria.objects.all()
#    serializer_class = CategoriaSerializer

class CategoriaViewSet(viewsets.ModelViewSet):  # Rest Full
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer


