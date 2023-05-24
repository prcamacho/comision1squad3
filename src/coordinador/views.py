from django.shortcuts import render
from .models import Coordinador
# Create your views here.

def listado_coodinadores(request):
    coordinadores=Coordinador.objects.all()
    return render(request,'coordinador/listado_coordinadores.html',{'coodinadores':coordinadores})
