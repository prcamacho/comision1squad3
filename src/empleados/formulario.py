from django import forms
from .models import Empleado
from django.forms import ModelForm
#Creacion de formulario 
class FormularioEmpleado(forms.Form):
    nombre = forms.CharField(max_length=20)
    apellido = forms.CharField(max_length=20)
    numero_legajo = forms.IntegerField()
    
class EditarFormularioEmpleado(forms.ModelForm):
    class Meta:
        model = Empleado
        fields = ["nombre","apellido","numero_legajo"]