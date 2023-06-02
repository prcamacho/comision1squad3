from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import FormReserva
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

# def modificar_reserva(request,id):
#     reserva = get_object_or_404(Reserva, id=id)
#     if request.method == 'POST':
#         formulario = EditarFormularioReserva(request.POST, instance=reserva)
#         if formulario.is_valid():
#             formulario.save()
#             return HttpResponseRedirect("/reservas/listado")
#     else:
#         formulario = EditarFormularioReserva(instance=reserva)
#         return render(request, 'reservas/nuevo.html', {'form': formulario}) 