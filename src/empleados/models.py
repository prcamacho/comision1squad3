from django.db import models
from django import forms
# Create your models here.

#Modelo del objeto Empleado

class Empleado (models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    numero_legajo = models.IntegerField()
    activo = models.BooleanField(default=True)
    
    #def __str__(self):
    #    return F"{self.nombre}, {self.apellido}, {self.numero_legajo}"
    
