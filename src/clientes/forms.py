from django import forms
from .models import Cliente


class FormCliente(forms.Form):
    nombre=forms.CharField(max_length=50, label='Nombres')
    apellido=forms.CharField(max_length=50, label='Apellidos')

class EditarFormCliente(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ["nombre","apellido"]