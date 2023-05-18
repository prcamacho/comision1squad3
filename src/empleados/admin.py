from django.contrib import admin
from .models import Empleado
# Register your models here.

#Opciones de busqueda y listado para Empleado
class AdminBusqueda(admin.ModelAdmin):
    list_display = ("nombre", "apellido", "numero_legajo", "activo")
    search_fields = ["nombre", "apellido"] 
    list_filter = ["activo"]

#Registro de Empleado al admin
admin.site.register(Empleado, AdminBusqueda)

