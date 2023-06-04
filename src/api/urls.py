from django.urls import path
from .views import *

app_name = "api"


urlpatterns = [
    path('servicios/',lista_servicios,name='lista_servicios'),
    path('servicios/<int:id>',datos_servicio,name='datos_servicio'),
]