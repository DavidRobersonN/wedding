from django.contrib import admin
from .models import People, Noivo, Noiva

@admin.register(Noivo)
class NoivoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'ativo')

@admin.register(Noiva)
class NoivaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'ativo')
