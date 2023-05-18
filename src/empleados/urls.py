from django.contrib import admin
from django.urls import path, include
from .views import nuevo_empleado

app_name = "empleados"

urlpatterns = [
    path('nuevo/', nuevo_empleado, name='nuevo_empleado'),
    #path('<int:pk>/', detalle_empleado, name='detalle_empleado'),
]