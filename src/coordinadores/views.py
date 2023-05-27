from django.shortcuts import render,get_object_or_404,redirect
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from .models import Coordinador
from .forms import EditarFormCoordinador, FormCoordinador

# Create your views here.

def activar_coordinador(request,id):
    coordinador_a_desactivar=get_object_or_404(Coordinador,id=id)
    coordinador_a_desactivar.activo=True
    coordinador_a_desactivar.save()
    return redirect(reverse('coordinadores:listado_coordinadores'))

def desactivar_coordinador(request,id):
    coordinador_a_desactivar=get_object_or_404(Coordinador,id=id)
    coordinador_a_desactivar.activo=False
    coordinador_a_desactivar.save()
    return redirect(reverse('coordinadores:listado_coordinadores'))

def listado_coordinadores(request):
    coordinadores=Coordinador.objects.all()
    return render(request,'coordinadores/listado.html',{'coordinadores':coordinadores})

def nuevo_coordinador(request):
    form=FormCoordinador()
    mensaje=None
    coordinador_nuevo=None
    if request.method=='POST':
        form=FormCoordinador(request.POST)
        if form.is_valid():
            cd=form.cleaned_data
            coordinador_nuevo=Coordinador.objects.create(nombre=cd['nombre'],
                                                         apellido=cd['apellido'],
                                                         numero_documento=cd['numero_documento'],
                                                         )
            mensaje="Coordinador Creado con exito"
    else:
        form=FormCoordinador()
    
    return render(request,'coordinadores/crear.html',{'form':form,
                                                    'mensaje':mensaje,
                                                    'coordinador_nuevo':coordinador_nuevo,
                                                    })
            

def modificar_coordinador(request, id):
    coordinador = get_object_or_404(Coordinador, id=id)
    if request.method == 'POST':
        formulario = EditarFormCoordinador(request.POST, instance=coordinador)
        if formulario.is_valid():
            formulario.save()
            return HttpResponseRedirect("/coordinadores/listado")
    else:
        formulario = EditarFormCoordinador(instance=coordinador)
    return render(request, 'coordinadores/crear.html', {'form': formulario}) 
