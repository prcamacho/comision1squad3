from django.shortcuts import render
from .models import Coordinador
# Create your views here.

def listado_coodinadores(request):
    coordinadores=Coordinador.objects.all()
    return render(request,'coordinadores/listado_coordinadores.html',{'coodinadores':coordinadores})
