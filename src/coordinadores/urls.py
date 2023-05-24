from django.urls import path
from .views import (desactivar_coordinador,
                    
)

app_name='coordinadores'

urlpatterns = [
    path('coordinadores/desactivar/<int: id>',desactivar_coordinador,name='desactivar_coordinador'),
]
