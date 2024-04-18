from django.contrib import admin
from .models import Noivo, Noiva, Padrinho

@admin.register(Noivo)
class NoivoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'facebook')
@admin.register(Noiva)
class NoivaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'facebook')
@admin.register(Padrinho)
class PadrinhoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'facebook')