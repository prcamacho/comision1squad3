from django.contrib import admin
from django.urls import path, include
from .views import *

app_name = "coordinadores"


urlpatterns = [
    path('coordinadores/activar/<int:id>',activar_coordinador,name='activar_coordinador'),
    path('coordinadores/desactivar/<int:id>',desactivar_coordinador,name='desactivar_coordinador'),
    path('coordinadores/listado/',listado_coodinadores,name='listado_coodinadores'),
    path('coordinadores/nuevo',nuevo_coordinador,name=nuevo_coordinador)
]