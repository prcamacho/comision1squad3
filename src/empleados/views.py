from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect,HttpResponse
from .formulario import FormularioEmpleado, EditarFormularioEmpleado
from .models import Empleado
from django.contrib import messages
from django.forms import ModelForm


# Create your views here.

def nuevo_empleado(request):
    
    if request.method == "POST":
        
        formulario = FormularioEmpleado(request.POST)
        
        if formulario.is_valid():
            cd = formulario.cleaned_data
            
            nuevo_Empleado = Empleado.objects.create(nombre = cd['nombre'],
                                                     apellido = cd['apellido'],
                                                     numero_legajo = cd ['numero_legajo'])
            messages.success(request, "Empleado agregado con exito")
            return HttpResponseRedirect ("/empleados/nuevo")
        
    else:
        formulario = FormularioEmpleado()
    return render(request, 'empleados/nuevo.html',{"form":formulario})

def modificar_empleado (request, id):
    empleado = get_object_or_404(Empleado, id=id)
    if request.method == 'POST':
        formulario = EditarFormularioEmpleado(request.POST, instance=empleado)
        if formulario.is_valid():
            formulario.save()
            return HttpResponseRedirect(f"/empleados/nuevo")
    else:
        formulario = EditarFormularioEmpleado(instance=empleado)
    return render(request, 'empleados/nuevo.html', {'form': formulario}) 
    
def activar_empleado(request, id):
    empleado = get_object_or_404(Empleado, id=id)
    if empleado.activo == False:
        empleado.activo = True
        messages.success(request, "Empleado activado con exito")
    else:
        messages.success(request, "Empleado ya esta activo")
    return render(request, 'empleados/activar.html')