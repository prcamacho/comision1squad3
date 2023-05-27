from django.contrib import admin
from .models import ReservaServicio,Servicio
# Register your models here.

class AdminReservaServicio(admin.ModelAdmin):
    list_display = ('cliente','responsable','empleado','servicio','precio','fecha_reserva','fecha_creacion')
    search_fields=['coordinador','cliente','empleado','servicio']

class ServicioAdmin(admin.ModelAdmin):
    list_display = ('nombre',)
    search_fields = ('nombre',) 
    list_filter = ('activo',)

admin.site.register(ReservaServicio,AdminReservaServicio,Servicio)
