from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('nueva_pelicula', views.nueva_pelicula, name='nueva_pelicula'),
    path('peliculas', views.peliculas, name='peliculas'),
    path('carga_pelicula', views.carga_pelicula, name='carga_pelicula'),
    path('localidades', views.localidades, name='localidades'),
    path('personas', views.personas, name='personas'),
]
