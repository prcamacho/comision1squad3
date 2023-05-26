from django.contrib import admin
from .models import Coordinador

# Register your models here.
class Coordinadoradmin(admin.ModelAdmin):
    list_display=('nombre','apellido','activo')
    search_fields=('nombre',)
    list_filter=('activo',)

admin.site.register(Coordinador,Coordinadoradmin)