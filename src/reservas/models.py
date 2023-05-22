from django.db import models
from clientes.models import Cliente
from coordinador.models import Coordinador
from empleados.models import Empleado
from servicio.models import Servicio

# Create your models here.

class ReservaServicio (models.Model):
    fecha_creacion=models.DateTimeField(auto_now_add=True)
    fecha_reserva=models.DateTimeField()
    cliente=models.ForeignKey(Cliente)
    responsable=models.ForeignKey(Coordinador)
    empleado=models.ForeignKey(Empleado)
    servicio=models.ForeignKey(Servicio)
    precio=models.DecimalField(decimal_places=2)
