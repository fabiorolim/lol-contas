"""lol URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path

from .views import dashboard, categoria, conta, categorias, contas, \
    editar_conta, deletar_conta, editar_categoria, deletar_categoria, simulador

urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('dashboard', dashboard, name='dashboard'),
    path('conta', conta, name='conta'),
    path('contas', contas, name='contas'),
    path('editar_conta/<int:id>', editar_conta, name='editar_conta'),
    path('deletar_conta/<int:id>', deletar_conta, name='deletar_conta'),
    path('categoria', categoria, name='categoria'),
    path('categorias', categorias, name='categorias'),
    path('editar_categoria/<int:id>', editar_categoria,
         name='editar_categoria'),
    path('deletar_categoria/<int:id>', deletar_categoria,
         name='deletar_categoria'),
    path('simulador', simulador, name='simulador')
]
