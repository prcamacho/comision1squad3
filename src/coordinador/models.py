from django.db import models
from datetime import datetime

# Create your models here.

class Coordinador(models.Model):
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    numero_documento=models.PositiveBigIntegerField()
    fecha_alta=models.DateTimeField(default=datetime.now())
    activo=models.BooleanField(default=True)