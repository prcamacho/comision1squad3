from rest_framework import serializers
from servicios.models import *
from clientes.models import *
from empleados.models import *
from coordinadores.models import * 

class ServicioSerializer(serializers.ModelSerializer):
    class Meta:
        model=Servicio
        fields=['id','nombre','precio']
        
class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model=Cliente
        fields=['id','nombre','apellido']
        
class EmpleadoSerializer(serializers.ModelSerializer):
    class Meta:
        model=Empleado
        fields=['id','nombre','apellido','numero_legajo']
        
class CoordinadorSerializer(serializers.ModelSerializer):
    class Meta:
        model=Coordinador
        fields=['id','nombre','apellido','numero_documento','fecha_alta']                        