from django.contrib import admin
from django.urls import path, include
from .views import activar_empleado, detalle_empleado

app_name = "empleados"

urlpatterns = [
    path('activar/', activar_empleado, name='activar_empleado'),
     path('<int:pk>/', detalle_empleado, name='detalle_empleado'),
]