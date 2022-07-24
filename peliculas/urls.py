from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('<int:pelicula_id>', views.pelicula_detalle, name='pelicula_detalle'),
    path('directores', views.directores, name='directores'),
    path('director/<int:director_id>', views.director_detalle, name='director_detalle'),
]
