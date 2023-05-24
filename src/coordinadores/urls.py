<<<<<<< HEAD:src/coordinador/urls.py
from django.contrib import admin
from django.urls import path, include
from .views import *

app_name = "coordinadores"

urlpatterns = [
    path('listado/',listado_coodinadores,name='listado_coodinadores'),
]
=======
from django.urls import path
from .views import (desactivar_coordinador,
                    
)

app_name='coordinadores'

urlpatterns = [
    path('coordinadores/desactivar/<int: id>',desactivar_coordinador,name='desactivar_coordinador'),
]
>>>>>>> rama_pc:src/coordinadores/urls.py
