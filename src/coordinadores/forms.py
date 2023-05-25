from django import forms
from .models import Coordinador

class FormCoordinador(forms.Form):
    nombre=forms.CharField(max_length=50, label='Nombres')
    apellido=forms.CharField(max_length=50, label='Apellidos')
    numero_documento=forms.IntegerField(label='DNI')
    
class EditarFormCoordinador(forms.ModelForm):
    class Meta:
        model = Coordinador
        fields = ["nombre","apellido","numero_documento"]
        
    