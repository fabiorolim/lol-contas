from django.contrib import admin

from core.models import (
    Categoria, Conta, Movimentacao, Orcamento,
    ValorOrcamentario, Parcela
)


class ContaAdmin(admin.ModelAdmin):
    list_display = ('id', 'descricao', 'valor', 'tipo', 'usuario')
    list_display_links = ('id', 'descricao')
    list_per_page = 20


class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('id', 'descricao', 'tipo', 'ativa')
    list_display_links = ('id', 'descricao')
    list_filter = ('descricao',)
    list_per_page = 20


admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Conta, ContaAdmin)
admin.site.register(Movimentacao)
admin.site.register(Orcamento)
admin.site.register(ValorOrcamentario)
admin.site.register(Parcela)
