import django.contrib.auth as auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import redirect, render

from lol.core.views import dashboard


# Create your views here.

def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        senha = request.POST['senha']

        print(email, senha)

        if email != '' or senha != '':

            if User.objects.filter(email=email).exists():
                nome = User.objects.filter(
                    email=email).values_list('username', flat=True).get()

                usuario = auth.authenticate(username=nome, password=senha)

                if usuario is not None:
                    auth.login(request, usuario)

                    return redirect(dashboard)

        else:
            return redirect(login)
    else:
        return render(request, 'autenticacao/login.html')


@login_required(login_url='login')
def logout(request):
    auth.logout(request)
    return redirect(login)
