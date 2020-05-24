from django.contrib import admin
from .models import Personas, Tarjetas

admin.site.register([Personas, Tarjetas])
