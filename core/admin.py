from django.contrib import admin
from .models import People, Noivo, Noiva

@admin.register(People)
class PeopleAdmin(admin.ModelAdmin):
    list_display = ('nome', 'modificado')

@admin.register(Noivo)
class Noivo(admin.ModelAdmin):
    list_display = ('nome', 'modificado')

@admin.register(Noiva)
class Noiva(admin.ModelAdmin):
    list_display = ('nome', 'modificado')