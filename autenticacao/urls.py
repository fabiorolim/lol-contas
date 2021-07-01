from django.urls import path

from .views import login, logout

urlpatterns = [
    path('entrar', login, name='login'),
    path('sair', logout, name='logout'),
]
