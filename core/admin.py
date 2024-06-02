from django.contrib import admin
from .models import Padrinho, Madrinha, Noiva, Noivo, Casamento, HistoriaDeAmor, Saudacao, NossoBlog


@admin.register(Padrinho)
class PadrinhoAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    exclude = ('noivo',)


@admin.register(Madrinha)
class MadrinhaAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    exclude = ('noiva',)


@admin.register(Noivo)
class NoivoAdmin(admin.ModelAdmin):
    list_display = ('nome',)


@admin.register(Noiva)
class NoivaAdmin(admin.ModelAdmin):
    list_display = ('nome',)


@admin.register(Casamento)
class CasamentoAdmin(admin.ModelAdmin):
    list_display = ('dataCerimonia',)


@admin.register(HistoriaDeAmor)
class HistoriaDeAmor(admin.ModelAdmin):
    list_display = ('titulo',)
    exclude = ('nome', 'facebook', 'twitter', 'instagram',)


@admin.register(Saudacao)
class SaudacoesAdmin(admin.ModelAdmin):
    pass


@admin.register(NossoBlog)
class NossoBlogAdmin(admin.ModelAdmin):
    list_display = ('titulo',)
    exclude = ('nome', 'facebook', 'twitter', 'instagram',)
