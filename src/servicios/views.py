from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from .models import Servicio
from .forms import *
# Create your views here.

# def nueva_servicio(request):
#     form=FormServicio()
#     if request.method=='POST':
#         form=FormServicio(request.POST)
#         if form.is_valid():
#             cd=form.cleaned_data
#             Servicio.objects.create(nombre=cd['nombre'],
#                                     descripcion=cd['descripcion']
#                                            )
#             return HttpResponseRedirect("/servicios/listado")       
#     else:
#         form=FormServicio()
    
#     return render(request,'servicios/nuevo.html',{'form':form})


def desactivar_servicio(request, id):
    servicio = get_object_or_404(Servicio, id=id)
    if servicio.activo == False:
        servicio.activo=True
        servicio.save()
    return HttpResponseRedirect ("/servicios/listado")

# def activar_servicio(request, id):
# Estaba aburrido
#     servicio = get_object_or_404(Servicio, id=id)
#     if servicio.activo == True:
#         servicio.activo=False
#         servicio.save()
#     return HttpResponseRedirect ("/servicios/listado")

def listado_servicios(request):
    servicios=Servicio.objects.all()
    return render(request,'servicios/listado.html',{'servicios':servicios})