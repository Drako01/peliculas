from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('nueva_pelicula', views.nueva_pelicula, name='nueva_pelicula'),
    path('peliculas', views.peliculas, name='peliculas'),
    path('carga_pelicula', views.carga_pelicula, name='carga_pelicula'),
    path('localidades', views.localidades, name='localidades'),
    path('localidad/<int:id_localidad>', views.localidad, name='localidad'),
    path('nueva_localidad', views.nueva_localidad, name='nueva_localidad'),
    path('personas', views.personas, name='personas'),
    path('nueva_persona', views.nueva_persona, name='nueva_persona'),    
]
