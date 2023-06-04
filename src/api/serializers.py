from rest_framework import serializers
from servicios.models import * 

class ServicioSerializer(serializers.ModelSerializer):
    class Meta:
        model=Servicio
        fields=['id','nombre','precio']