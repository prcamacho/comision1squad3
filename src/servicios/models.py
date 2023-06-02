from django.db import models

# Create your models here.

class Servicio(models.Model):
    nombre = models.CharField(max_length=30)
    descripcion = models.TextField(blank=True, null=True)
    precio=models.DecimalField()
    activo = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.nombre}"