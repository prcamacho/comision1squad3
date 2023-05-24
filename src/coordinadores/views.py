from django.shortcuts import render,get_object_or_404,redirect
from django.urls import reverse
from django.http import HttpResponse
from .models import Coordinador

# Create your views here.

def desactivar_coordinador(request,id):
    coordinador_a_desactivar=get_object_or_404(Coordinador,id=id)
    coordinador_a_desactivar.activo=False
    coordinador_a_desactivar.save
    mensaje=f"Coordinador {coordinador_a_desactivar.nombre} desactivado"
    return render(request,'coordinadores/desactivar.html',{'mensaje':mensaje})

def listado_coodinadores(request):
    coordinadores=Coordinador.objects.all()
    return render(request,'coordinadores/listado_coordinadores.html',{'coodinadores':coordinadores})
