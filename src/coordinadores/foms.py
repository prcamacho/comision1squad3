from django import forms
from .models import Coordinador

class FormCoordinador(forms.Form):
    nombre=forms.CharField(max_length=50)
    apellido=forms.CharField(max_length=50)
    numero_documento=forms.IntegerField()
    