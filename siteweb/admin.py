from django.contrib import admin
from .models import Plano, PlanoAdquirido


@admin.register(Plano)
class PlanoAdmin(admin.ModelAdmin):
    pass

@admin.register(PlanoAdquirido)
class PlanoAdquiridoAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'plano', 'data_adquirida')