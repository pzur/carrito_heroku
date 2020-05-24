from django.urls import path,include
from . import views


app_name = "apis_user"



urlpatterns = [
    path('registrarusuario/', views.RegistrarUsuarios.as_view()),
    path('autenticar/', views.LoginView.as_view()),

]


#endpoints

#http://127.0.0.1:8000/apis_user/registrarusuario/
#http://127.0.0.1:8000/apis_user/autenticar/