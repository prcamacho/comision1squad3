from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect,HttpResponse
from .formulario import FormularioEmpleado
from .models import Empleado
from django.contrib import messages


# Create your views here.

def nuevo_empleado(request):
    
    if request.method == "POST":
        
        formulario = FormularioEmpleado(request.POST)
        
        if formulario.is_valid():
            cd = formulario.cleaned_data
            
            nuevo_Empleado = Empleado.objects.create(nombre = cd['nombre'],
                                                     apellido = cd['apellido'],
                                                     numero_legajo = cd ['numero_legajo'])
            messages.success(request, "Empleado agregado con exito")
            return HttpResponseRedirect ("/empleados/nuevo")
        
    else:
        formulario = FormularioEmpleado()
    return render(request, 'empleados/nuevo.html',{"form":formulario})

#def detalle_empleado(request, pk):
#   mi_empleado = get_object_or_404(Empleado, id=pk)
#   html = "<html><body><h1>Listado de empleados</h1>"
#   html += f"<p>{mi_empleado}</p>"
#   html += "</body></html>"
#   
#   return HttpResponse(html)


def desactivar_empleado(request,pk):
    empleado=get_object_or_404(Empleado,id=pk)
    empleado.activo=False
    html = "<html><body><h1>Empleado desactivado</h1>"
    html += f"<p>{empleado}</p>"
    html += "</body></html>"
    empleado.save()
    return HttpResponse(html)
