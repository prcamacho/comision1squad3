from django.http import HttpResponseRedirect
from django.shortcuts import render,get_object_or_404
from .forms import *
from .models import ReservaServicio
# Create your views here.

def nueva_reserva(request):
    form=FormReserva()
    if request.method=='POST':
        form=FormReserva(request.POST)
        if form.is_valid():
            cd=form.cleaned_data
            ReservaServicio.objects.create(fecha_reserva=cd['fecha_reserva'],
                                           cliente=cd['cliente'],
                                           responsable=cd['responsable'],
                                           empleado=cd['empleado'],
                                           servicio=cd['servicio'],
                                           precio=cd['precio']
                                           )
            return HttpResponseRedirect("/reservas/listado")       
    else:
        form=FormReserva()
    
    return render(request,'reservas/nuevo.html',{'form':form})

def listado_reservas(request):
    reservas=ReservaServicio.objects.all()
    return render(request,'reservas/listado.html',{'reservas':reservas})

def modificar_reserva(request,id):
    reserva = get_object_or_404(ReservaServicio, id=id)
    if request.method == 'POST':
        formulario = EditarFormReserva(request.POST, instance=reserva)
        if formulario.is_valid():
            formulario.save()
            return HttpResponseRedirect("/reservas/listado")
    else:
        formulario = EditarFormReserva(instance=reserva)
        return render(request, 'reservas/nuevo.html', {'form': formulario}) 
    
def eliminar_reserva(request,id):
    reserva = get_object_or_404(ReservaServicio, id=id)
    reserva.delete()
    reserva.save()
    reservas=ReservaServicio.objects.all()
    return render(request,'reservas/listado.html',{'reservas':reservas})