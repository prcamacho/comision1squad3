from django import forms
from .models import Servicio

class FormularioServicio(forms.Form):
    nombre = forms.CharField(max_length=30)
    descripcion = forms.Textarea()
    numero_legajo = forms.IntegerField()

class EditarFormularioServicio(forms.ModelForm):
    class Meta:
        model = Servicio
        fields = ["nombre","descripcion","precio"]