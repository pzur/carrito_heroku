from django.urls import path,include
from . import views
from rest_framework import routers


app_name = "apis_categorias"
router = routers.DefaultRouter()
router.register('List_Categorias_Productos', views.CategoriaViewSet)


urlpatterns = [
    path('', include(router.urls)),
    #path('List_Categorias/', views.CategoriaViewSet.as_view()),

]


# "http://127.0.0.1:8000/apis_categorias/List_Categorias_Productos/"