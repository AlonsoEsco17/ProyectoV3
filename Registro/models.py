from django.db import models

# Create your models here.

class Equipo (models.Model):
    nombre= models.CharField(max_length=20)
    pais = models.CharField(max_length=20)
    
    def __str__(self):
        return self.nombre

class Jugador (models.Model):
    equipo = models.ForeignKey(Equipo, null = True, blank = True, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    edad = models.IntegerField()
    año = models.IntegerField()
    
    def __str__(self):
        return self.nombre
    


