from django.db import models
from django.contrib.auth.models import User


class Personas(models.Model):
    # Clientes,Despachador,Administrador,Operador
    direccion = models.CharField(max_length=300, null=True, blank=True)
    correo = models.EmailField(blank=True, null=True)
    telefono = models.CharField(max_length=15, null=True, blank=True)
    ruc = models.CharField(max_length=15, null=True, blank=True)
    foto = models.ImageField(upload_to='Personas/Fotos', null=True, blank=True)
    estado = models.BooleanField(default=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='Personas')
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
