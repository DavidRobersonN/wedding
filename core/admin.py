from django.contrib import admin
from .models import Padrinho, Madrinha, Noiva, Noivo


@admin.register(Padrinho)
class PadrinhoAdmin(admin.ModelAdmin):
    list_display = ('nome',)

@admin.register(Madrinha)
class MadrinhaAdmin(admin.ModelAdmin):
    list_display = ('nome',)

@admin.register(Noivo)
class NoivoAdmin(admin.ModelAdmin):
    list_display = ('nome',)

@admin.register(Noiva)
class NoivaAdmin(admin.ModelAdmin):
    list_display = ('nome', )
