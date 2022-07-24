from django.db import models


class Director(models.Model):
    nombre = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField('Fecha de Nacimiento')
    fecha_muerte = models.DateField('Fecha de Fallecimiento', null=True, blank = True)
    bio = models.TextField(null=True, blank = True)

    def __str__(self):
        return self.nombre


class Pelicula(models.Model):
    nombre = models.CharField(max_length=200)
    fecha = models.DateField('Fecha de Realización')
    duracion = models.IntegerField()
    sinopsis = models.TextField()
    director = models.ForeignKey(Director, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre
