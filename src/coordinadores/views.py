from django.shortcuts import render,get_object_or_404,redirect
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from .models import Coordinador
from .forms import EditarFormCoordinador

# Create your views here.

def activar_coordinador(request,id):
    coordinador_a_desactivar=get_object_or_404(Coordinador,id=id)
    coordinador_a_desactivar.activo=True
    coordinador_a_desactivar.save
    mensaje=f"Coordinador {coordinador_a_desactivar.nombre} activado"
    return render(request,'coordinadores/activar.html',{'mensaje':mensaje})

def desactivar_coordinador(request,id):
    coordinador_a_desactivar=get_object_or_404(Coordinador,id=id)
    coordinador_a_desactivar.activo=False
    coordinador_a_desactivar.save
    mensaje=f"Coordinador {coordinador_a_desactivar.nombre} desactivado"
    return render(request,'coordinadores/desactivar.html',{'mensaje':mensaje})

def listado_coodinadores(request):
    coordinadores=Coordinador.objects.all()
    return render(request,'coordinadores/listado_coordinadores.html',{'coodinadores':coordinadores})

def modificar_coordinador (request, id):
    coordinador = get_object_or_404(Coordinador, id=id)
    if request.method == 'POST':
        formulario = EditarFormCoordinador(request.POST, instance=coordinador)
        if formulario.is_valid():
            formulario.save()
            return HttpResponseRedirect("/coordinador/listado")
    else:
        formulario = EditarFormCoordinador(instance=coordinador)
    return render(request, 'coodinador/nuevo_coordinador.html', {'form': formulario}) 
