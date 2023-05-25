from django.contrib import admin
from django.urls import path, include
from .views import *

app_name = "coordinadores"


urlpatterns = [
    path('activar/<int:id>/',activar_coordinador,name='activar_coordinador'),
    path('desactivar/<int:id>/',desactivar_coordinador,name='desactivar_coordinador'),
    path('listado/',listado_coodinadores,name='listado_coodinadores'),
    path('nuevo/',nuevo_coordinador,name='nuevo_coordinador'),
]