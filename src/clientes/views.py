from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import Cliente
from .forms import FormCliente, EditarFormCliente

# Create your views here.
def desactivar_cliente(request,id):
    cliente_a_desactivar=get_object_or_404(Cliente,id=id)
    cliente_a_desactivar.activo=False
    cliente_a_desactivar.save
    mensaje=f"Cliente {cliente_a_desactivar.nombre} desactivado"
    return render(request,'clientes/desactivar.html',{'mensaje':mensaje})

def listado_clientes(request):
    clientes=Cliente.objects.all()
    return render(request,'clientes/listado.html',{'clientes':clientes})

def modificar_cliente(request,id):
    cliente = get_object_or_404(Cliente, id=id)
    if request.method == 'POST':
        formulario = EditarFormCliente(request.POST, instance=cliente)
        if formulario.is_valid():
            formulario.save()
            return HttpResponseRedirect("/cliente/listado")
    else:
        formulario = EditarFormCliente(instance=cliente)
    return render(request, 'cliente/crear.html', {'form': formulario}) 