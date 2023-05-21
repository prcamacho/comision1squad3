from django.contrib import admin
from django.urls import path, include
from .views import nuevo_empleado, modificar_empleado, activar_empleado


app_name = "empleados"

urlpatterns = [
    path('nuevo/', nuevo_empleado, name='nuevo_empleado'),
    path('modificar/<int:id>', modificar_empleado, name= 'modificar_empleado'),
    path('activar/<int:id>',activar_empleado, name='activar_empleado')
]