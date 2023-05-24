from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from .models import Coordinador
from .foms import *
# Create your views here.

def listado_coodinadores(request):
    coordinadores=Coordinador.objects.all()
    return render(request,'coodinador/listado_coordinadores.html',{'coodinadores':coordinadores})

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