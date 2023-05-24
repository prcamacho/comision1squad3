from django.contrib import admin
from .models import Cliente
# Register your models here.


class AdminBusqueda(admin.ModelAdmin):
    list_display = ("nombre", "apellido", "activo")
    search_fields = ["nombre", "apellido"] 
    list_filter = ["activo"]

#Registro de Empleado al admin
admin.site.register(Cliente, AdminBusqueda)