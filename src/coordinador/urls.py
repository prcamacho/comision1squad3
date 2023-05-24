from django.contrib import admin
from django.urls import path, include
from .views import *

app_name = "coordinadores"

urlpatterns = [
    path('listado/',listado_coodinadores,name='listado_coodinadores'),
    path('modificar/<int:id>', modificar_coordinador, name= 'modificar_coordinador'),
]