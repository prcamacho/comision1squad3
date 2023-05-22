from django.contrib import admin
from django.urls import path, include
from .views import *

app_name = "empleados"

urlpatterns = [
    path('nuevo/', nuevo_empleado, name='nuevo_empleado'),
    path('modificar/<int:id>', modificar_empleado, name= 'modificar_empleado'),
    path('activar/<int:id>',activar_empleado, name='activar_empleado')
    path('desactivar/<int:pk>', desactivar_empleado, name='desactivar_empleado'),
    path('listado/',listado_empleados,name='listado_empleados'),
]