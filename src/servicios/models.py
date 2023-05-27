from django.db import models

# Create your models here.

class Servicio(models.Model):
    nombre = models.CharField(max_length=30)
    descripcion = models.TextField(blank=True, null=True)
    activo = models.BooleanField(default=True)
