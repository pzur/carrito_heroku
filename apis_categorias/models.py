from django.db import models
from django.contrib.auth.models import User


class Categoria(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True, null=True)
    estado = models.BooleanField(default=True)
    #user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True,related_name="categoria")

    def __str__(self):
        return self.nombre
