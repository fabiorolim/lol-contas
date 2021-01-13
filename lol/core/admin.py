from django.contrib import admin

from lol.core.models import Categoria, Conta

# Register your models here.

class ContaAdmin(admin.ModelAdmin):
    list_display = ('id', 'descricao', 'valor', 'tipo', 'usuario')
    list_display_links = ('id', 'descricao')
    list_filter = ('categoria',)
    list_per_page = 20


class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('id', 'descricao', 'ativa')
    list_display_links = ('id', 'descricao')
    list_filter = ('descricao',)
    list_per_page = 20

admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Conta, ContaAdmin)