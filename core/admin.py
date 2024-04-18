from django.contrib import admin
from .models import Padrinho, Noiva, Noivo

@admin.register(Padrinho)
class PadrinhoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'instagram')

@admin.register(Noiva)
class NoivaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'instagram')

@admin.register(Noivo)
class NoivoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'instagram')