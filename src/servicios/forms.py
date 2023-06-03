from django import forms
from .models import Servicio

class FormularioServicio(forms.Form):
    nombre = forms.CharField(max_length=30)
    descripcion = forms.CharField(widget=forms.Textarea(attrs={'rows':5, 'cols':20}))
    precio= forms.DecimalField(decimal_places=2, max_digits=10)

class EditarFormularioServicio(forms.ModelForm):
    class Meta:
        model = Servicio
        fields = ["nombre","descripcion","precio"]