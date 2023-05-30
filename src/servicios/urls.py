from django.contrib import admin
from django.urls import path, include
from .views import *

app_name = "servicios"

urlpatterns = [
    path('desactivar/<int:pk>', desactivar_servicio, name='desactivar_servicio'),
]