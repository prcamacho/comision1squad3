from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from .models import Servicio
# Create your views here.

def desactivar_servicio(request, id):
    servicio = get_object_or_404(Servicio, id=id)
    if servicio.activo == False:
        servicio.activo=True
        servicio.save()
    return HttpResponseRedirect ("/servicios/listado")