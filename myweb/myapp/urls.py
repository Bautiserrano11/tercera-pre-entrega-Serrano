from django.urls import path
from .views import lista_libros, agregar_datos, busqueda

urlpatterns = [
    path('lista_libros/', lista_libros, name='lista_libros'),
    path('agregar_datos/', agregar_datos, name='agregar_datos'),
    path('busqueda/', busqueda, name='busqueda'),
]
