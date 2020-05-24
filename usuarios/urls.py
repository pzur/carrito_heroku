from django.urls import path
from . import views
from rest_framework import routers
# from .views import *
from django.conf.urls import include

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register('List_Categorias', views.CategoriaViewSet)
router.register('List_ProductosIngredientes', views.ProductosingredientesViewSet)
router.register('List_CategoriasProductos', views.CategoriasproductossViewSet)
router.register('List_Users', views.UserViewSet)

router.register('List_Fotos_Personas', views.PersonaViewSet)

urlpatterns = [
    path('', views.all_productos),
    path('detail/<int:id>', views.detail_productos),
    path('busqueda/<nombre>', views.filtar_productos),
    path('prodcat/', views.productosycategorias),
    path('platosfotos/', views.productos_fotos),
    path('apis_carrito/', include(router.urls)),

    path('prodsql/', views.all_platos_sql),
    path('prodsqlprocedure/', views.all_platos_sql_procedure),
    path('prod_cat/<int:idcat>', views.all_platos_categoria),

]
