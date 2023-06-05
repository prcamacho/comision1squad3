from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from servicios.models import *
from .serializers import *
from django.shortcuts import get_object_or_404
# Create your views here.

@api_view(http_method_names=['GET'])
def lista_servicios(request):
    servicios=Servicio.objects.all()
    serializer=ServicioSerializer(instance=servicios,many=True)
    repuesta={
        'Mensaje':'Lista de Servicios',
        'Datos':serializer.data
    }
    return Response(data=repuesta,status=status.HTTP_200_OK)

@api_view(http_method_names=['GET'])
def datos_servicio(request,id:int):
    servicios=get_object_or_404(Servicio,id=id)
    serializer=ServicioSerializer(instance=servicios)
    repuesta={
        'Datos Servicio':serializer.data
    }
    return Response(data=repuesta,status=status.HTTP_200_OK)

@api_view(http_method_names=['GET'])
def lista_clientes(request):
    clientes=Cliente.objects.all()
    serializer=ClienteSerializer(instance=clientes,many=True)
    repuesta={
        'Mensaje':'Lista de Clientes',
        'Datos':serializer.data
    }
    return Response(data=repuesta,status=status.HTTP_200_OK)

@api_view(http_method_names=['GET'])
def datos_cliente(request,id:int):
    cliente=get_object_or_404(Cliente,id=id)
    serializer=ClienteSerializer(instance=cliente)
    repuesta={
        'Datos Cliente':serializer.data
    }
    return Response(data=repuesta,status=status.HTTP_200_OK)

@api_view(http_method_names=['GET'])
def lista_empleados(request):
    empleados=Empleado.objects.all()
    serializer=EmpleadoSerializer(instance=empleados,many=True)
    repuesta={
        'Mensaje':'Lista de Empleados',
        'Datos':serializer.data
    }
    return Response(data=repuesta,status=status.HTTP_200_OK)

@api_view(http_method_names=['GET'])
def datos_empleado(request,id:int):
    empleado=get_object_or_404(Empleado,id=id)
    serializer=EmpleadoSerializer(instance=empleado)
    repuesta={
        'Datos Empleado':serializer.data
    }
    return Response(data=repuesta,status=status.HTTP_200_OK)

@api_view(http_method_names=['GET'])
def lista_coordinadores(request):
    coordinadores=Coordinador.objects.all()
    serializer=CoordinadorSerializer(instance=coordinadores,many=True)
    repuesta={
        'Mensaje':'Lista de Coordinadores',
        'Datos':serializer.data
    }
    return Response(data=repuesta,status=status.HTTP_200_OK)

@api_view(http_method_names=['GET'])
def datos_coordinador(request,id:int):
    coordinador=get_object_or_404(Coordinador,id=id)
    serializer=CoordinadorSerializer(instance=coordinador)
    repuesta={
        'Datos coordinador':serializer.data
    }
    return Response(data=repuesta,status=status.HTTP_200_OK)