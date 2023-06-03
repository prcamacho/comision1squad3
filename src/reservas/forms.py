from django import forms
from .models import ReservaServicio
from clientes.models import Cliente
from coordinadores.models import Coordinador
from empleados.models import Empleado
from servicios.models import Servicio

class FormReserva(forms.ModelForm):
    fecha_creacion=forms.DateTimeField()
    fecha_reserva=forms.DateTimeField()
    cliente=forms.ModelChoiceField(queryset=Cliente.objects.filter(activo=True))
    responsable=forms.ModelChoiceField(queryset=Coordinador.objects.filter(activo=True))
    empleado=forms.ModelChoiceField(queryset=Empleado.objects.filter(activo=True))
    servicio=forms.ModelChoiceField(queryset=Servicio.objects.filter(activo=True))
    precio=forms.DecimalField(decimal_places=2, max_digits=10)
