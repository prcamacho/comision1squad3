from django.contrib import admin
from django.urls import path, include
from .views import *

app_name = "empleados"

urlpatterns = [
    path('nuevo/', nueva_reserva,name='nueva_reserva')
]