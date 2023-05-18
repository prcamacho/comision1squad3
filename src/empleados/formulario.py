from django import forms

#Creacion de formulario 
class FormularioEmpleado(forms.Form):
    nombre = forms.CharField(max_length=20)
    apellido = forms.CharField(max_length=20)
    numero_legajo = forms.IntegerField()
    
    