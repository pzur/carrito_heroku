from django.urls import path
from . import views

app_name = "apis_productos"

urlpatterns = [

    path('List_Productos/', views.ProductosListView.as_view()),
    path('Detail_Productos/<id>', views.ProductoDetailView.as_view()),

]

#http://127.0.0.1:8000/apis_productos/List_Productos/
#http://127.0.0.1:8000/apis_productos/Detail_Productos/2
