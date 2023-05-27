from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Cliente
from .forms import FormCliente, EditarFormCliente

# Create your views here.
def nuevo_cliente(request):
    form=FormCliente()
    if request.method=='POST':
        form=FormCliente(request.POST)
        if form.is_valid():
            cd=form.cleaned_data
            Cliente.objects.create(nombre=cd['nombre'],
                                                        apellido=cd['apellido']
                                                        )
            return HttpResponseRedirect("/clientes/listado")       
    else:
        form=FormCliente()
    
    return render(request,'clientes/crear.html',{'form':form})

def desactivar_cliente(request,id):
    cliente_a_desactivar=get_object_or_404(Cliente,id=id)
    cliente_a_desactivar.activo=False
    cliente_a_desactivar.save()
    #mensaje=f"Cliente {cliente_a_desactivar.nombre} desactivado"
    #return render(request,'clientes/desactivar.html',{'mensaje':mensaje})
    return redirect(reverse('clientes:listado_clientes'))

def activar_cliente(request,id):
    cliente_a_desactivar=get_object_or_404(Cliente,id=id)
    cliente_a_desactivar.activo=True
    cliente_a_desactivar.save()
    return redirect(reverse('clientes:listado_clientes'))

def listado_clientes(request):
    clientes=Cliente.objects.all()
    return render(request,'clientes/listado.html',{'clientes':clientes})

def nuevo_cliente(request):
    form=FormCliente()
    mensaje=None
    cliente_nuevo=None
    if request.method=='POST':
        form=FormCliente(request.POST)
        if form.is_valid():
            cd=form.cleaned_data
            cliente_nuevo=Cliente.objects.create(nombre=cd['nombre'],
                                                         apellido=cd['apellido'],
                                                         numero_documento=cd['numero_documento'],
                                                         )
            mensaje="Cliente Creado con exito"
    else:
        form=FormCliente()
    
    return render(request,'clientes/crear.html',{'form':form,
                                                    'mensaje':mensaje,
                                                    'cliente_nuevo':cliente_nuevo,
                                                    })


def modificar_cliente(request,id):
    cliente = get_object_or_404(Cliente, id=id)
    if request.method == 'POST':
        formulario = EditarFormCliente(request.POST, instance=cliente)
        if formulario.is_valid():
            formulario.save()
            return HttpResponseRedirect("/clientes/listado")
    else:
        formulario = EditarFormCliente(instance=cliente)
    return render(request, 'clientes/editar.html', {'form': formulario}) 