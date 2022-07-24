from multiprocessing import context
from tempfile import template
from django.shortcuts import render
from .models import Director, Pelicula

def index(request):
    listado_peliculas = Pelicula.objects.order_by('-fecha')[:5]
    context = {
        'listado_peliculas': listado_peliculas
    }

    return render(request, 'peliculas/index.html',context)

def pelicula_detalle(request, pelicula_id):
    pelicula = Pelicula.objects.get(pk=pelicula_id)
    context = {
        'pelicula': pelicula
    }

    return render(request, 'peliculas/detalle_pelicula.html', context)

def directores(request):
    listado_directores = Director.objects.order_by('-nombre')[:5]
    context = {
        'listado_directores': listado_directores
    }

    return render(request, 'directores/index.html',context)

def director_detalle(request, director_id):
    director = Director.objects.get(pk=director_id)
    context = {
        'director': director
    }
    
    return render(request, 'directores/detalle_director.html', context)
