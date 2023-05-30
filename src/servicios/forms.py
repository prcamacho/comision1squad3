from django import forms
from .models import Servicio


class EditarFormularioEmpleado(forms.ModelForm):
    class Meta:
        model = Servicio
        fields = ["nombre","descripcion"]