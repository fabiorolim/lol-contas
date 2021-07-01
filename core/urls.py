from django.urls import path

from .views import (
    dashboard, simulador, movimentacoes, movimentacao,
    editar_movimentacao, editar_categoria, categoria, categorias,
    deletar_categoria, deletar_movimentacao
)

urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('dashboard', dashboard, name='dashboard'),
    path('movimentacao', movimentacao, name='movimentacao'),
    path('contas', movimentacoes, name='movimentacoes'),
    path('editar_movimentacao/<int:id>', editar_movimentacao,
         name='editar_movimentacao'),
    path('deletar_movimentacao/<int:id>', deletar_movimentacao,
         name='deletar_movimentacao'),
    path('categoria', categoria, name='categoria'),
    path('categorias', categorias, name='categorias'),
    path('editar_categoria/<int:id>', editar_categoria,
         name='editar_categoria'),
    path('deletar_categoria/<int:id>', deletar_categoria,
         name='deletar_categoria'),
    path('simulador', simulador, name='simulador')
]
