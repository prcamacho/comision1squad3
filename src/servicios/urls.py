from django.contrib import admin
from django.urls import path, include
from .views import *

app_name = "servicios"

urlpatterns = [
    path('nuevo/', nuevo_servicio, name='nuevo_servicio'),
    path('listado/',listado_servicios,name='listado_servicios'),
    path('desactivar/<int:pk>', desactivar_servicio, name='desactivar_servicio'),
    path('activar/<int:pk>', activar_servicio, name='activar_servicio'),
    path('modificar/<int:id>/', modificar_servicio,name='modificar_servicio'),
]