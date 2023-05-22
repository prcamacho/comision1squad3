from django.contrib import admin
from django.urls import path, include
from .views import *

app_name = "empleados"

urlpatterns = [
    path('nuevo/', nuevo_empleado, name='nuevo_empleado'),
    #path('<int:pk>/', detalle_empleado, name='detalle_empleado'),
    path('desactivar/<int:pk>', desactivar_empleado, name='desactivar_empleado'),
    path('listado/',listado_empleados,name='listado_empleados'),
]