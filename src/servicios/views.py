from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from .models import Servicio
from .forms import *
# Create your views here.

def nuevo_servicio(request):
    form=FormularioServicio()
    if request.method=='POST':
        form=FormularioServicio(request.POST)
        if form.is_valid():
            cd=form.cleaned_data
            Servicio.objects.create(nombre=cd['nombre'],
                                    descripcion=cd['descripcion'],
                                    precio=cd['precio']
                                           )
            return HttpResponseRedirect("/servicios/listado")       
    else:
        form=FormularioServicio()
    
    return render(request,'servicios/nuevo.html',{'form':form})

def desactivar_servicio(request, pk):
    servicio = get_object_or_404(Servicio, id=pk)
    if servicio.activo == True:
        servicio.activo=False
        servicio.save()
    return HttpResponseRedirect ("/servicios/listado")

def activar_servicio(request, pk):
    servicio = get_object_or_404(Servicio, id=pk)
    if servicio.activo == False:
        servicio.activo=True
        servicio.save()
    return HttpResponseRedirect ("/servicios/listado")

def listado_servicios(request):
    servicios=Servicio.objects.all()
    return render(request,'servicios/listado.html',{'servicios':servicios})