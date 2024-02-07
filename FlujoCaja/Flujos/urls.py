from django.urls import path, include
from .views import *

 
urlpatterns = [
    #path('Flujos/', include('Flujos.urls')),
    path('', home, name = "home"),
    path('Locales', ver_locales, name = "Locales"),
    path('Productos', ver_productos, name = "Productos"),
    path('Entregas', ver_entregas, name = "Entregas"),
    path('Repartidores', ver_repartidores, name = "Repartidores"),

    path('FormularioLocal', localForm, name = "FormularioLocal"),
    path('FormularioProducto', productoForm, name = "FormularioProducto"),
    path('FormularioRepartidor', repartidorForm, name = "FormularioRepartidor"),

    path('buscar', buscar, name = "buscar"),
    path('buscarProd', buscarProd, name = "buscarProd"),
    

]
