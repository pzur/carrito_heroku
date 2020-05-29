from rest_framework import generics
from django.contrib.auth.models import User
import json
from django.http import HttpResponse
from rest_framework.views import APIView
from django.contrib.auth import authenticate
from .models import Personas



# Vistas Basadas en Clases Controlando todo el Modelo de Usuarios

class RegistrarUsuarios(generics.CreateAPIView): #Solo Registrar datos en el modelo

    
    def post(self, request, *args, **kwargs):
        # Creando en Nuevo Usuario
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        #first_name = request.POST.get('first_name')
        #last_name = request.POST.get('last_name')
        user = User.objects.create_user(username, email, password)
        #user.first_name = first_name
        #user.last_name = last_name
        user.save()
        data = {'detail': 'usuario creado con exito'}
        respuesta = json.dumps(data)
        return HttpResponse(respuesta, content_type='application/json')


class LoginView(APIView):
    
    def post(self, request, ):
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username=username, password=password)
        if user:
            data = {"correcto": "Son las credenciales"}
            # # trae informacion del modelo persona de acuerdo al ID
            # userpersona = Personas.objects.get(user_id=user.id)
            # data = {"nombre": user.first_name,
            #         "apellido": user.last_name,
            #         "telefono": userpersona.telefono,
            #         "ruc": userpersona.ruc}
        else:
            data = {"error": "No Son las Credenciales"}
        respuesta = json.dumps(data)
        return HttpResponse(respuesta, content_type='application/json')

# Serializar Foto
# https://stackoverrun.com/es/q/9792839
