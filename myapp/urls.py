from django.urls import path, include
from . import views
from rest_framework import routers


router = routers.DefaultRouter()
router.register('establecimientos', views.ProductosViewset)
router.register('categoria', views.CategoriasViewset)

# localhost:8000/api/producto/


urlpatterns = [
    path('', views.index, name='index'),
    path('establecimientos/', views.establecimientos, name='establecimientos'),
    path('establecimiento/<slug:slug>', views.EstablecimientoDetailView.as_view(), name='detalle'),
    path('contacto/', views.contacto, name='contacto'),
    path('registro/', views.registro, name='registro'),
    path('agregar-establecimiento/', views.agregar_producto, name='agregar_establecimiento'),
    path('listar-establecimiento/', views.listar_producto, name='listar_establecimiento'),
    path('modificar-establecimiento/<id>/',
         views.modificar_producto, name='modificar_establecimiento'),
    path('eliminar-establecimiento/<id>/',
         views.eliminar_producto, name='eliminar_establecimiento'),
    path('api/', include(router.urls)),

]
