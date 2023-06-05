from django.urls import path
from .views import *

app_name = "api"


urlpatterns = [
    path('servicios/',lista_servicios,name='lista_servicios'),
    path('servicios/<int:id>',datos_servicio,name='datos_servicio'),
    path('clientes/',lista_clientes,name='lista_clientes'),
    path('clientes/<int:id>',datos_cliente,name='datos_cliente'),
    path('empleados/',lista_empleados,name='lista_empleados'),
    path('empleados/<int:id>',datos_empleado,name='datos_empleado'),
    path('coordinadores/',lista_coordinadores,name='lista_coordinadores'),
    path('coordinadores/<int:id>',datos_coordinador,name='datos_coordinador'),
]