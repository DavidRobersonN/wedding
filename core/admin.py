from django.contrib import admin
from .models import Padrinho, Noiva

@admin.register(Padrinho)
class PadrinhoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'instagram')

@admin.register(Noiva)
class NoivaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'instagram')
