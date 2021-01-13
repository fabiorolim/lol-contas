import json

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.models import Sum
from django.shortcuts import render, redirect, get_object_or_404

from .forms import CategoriaForm, ContaForm
from .models import Conta, Categoria


# Create your views here.

@login_required(login_url='login')
def dashboard(request):
    usuario_logado = get_object_or_404(User, pk=request.user.id)

    total_receber = Conta.objects.filter(usuario=usuario_logado).filter(
        tipo='R').aggregate(
        Sum('valor'))

    total_pagar = Conta.objects.filter(usuario=usuario_logado).filter(
        tipo='P').aggregate(
        Sum('valor'))

    valor_total_receber = 0
    if total_receber['valor__sum'] != None:
        valor_total_receber = total_receber['valor__sum']

    valor_total_pagar = 0
    if total_pagar['valor__sum'] != None:
        valor_total_pagar = total_pagar['valor__sum']

    saldo = valor_total_receber - valor_total_pagar

    # Query gráfico área

    valores_categorias = Conta.objects.values('categoria__descricao').annotate(
        Sum('valor')).filter(usuario=usuario_logado).filter(tipo='P').order_by(
        'valor__sum')

    categorias = []
    for vc in valores_categorias:
        categorias.append(vc['categoria__descricao'])

    valores_c = []
    for vc in valores_categorias:
        valores_c.append(float(vc['valor__sum']))

    # Query gráfico linha

    valores_mes = Conta.objects.values('data__month').annotate(
        Sum('valor')).filter(usuario=usuario_logado).filter(tipo='P').order_by(
        'data__month')

    meses = []
    for vm in valores_mes:
        meses.append(vm['data__month'])

    valores_m = []
    for vm in valores_mes:
        valores_m.append(float(vm['valor__sum']))

    context = {
        'total_pagar': valor_total_pagar,
        'total_receber': valor_total_receber,
        'saldo': saldo,
        'categorias': json.dumps(categorias),
        'valores_categorias': json.dumps(valores_c),
        'qtd_categorias': json.dumps(len(categorias)),
        'meses': json.dumps(meses),
        'valores_meses': json.dumps(valores_m),
    }

    return render(request, 'core/index.html', context)


@login_required(login_url='login')
def conta(request):
    if request.method == 'GET':
        form = ContaForm()
        contexto = {'form': form}

        return render(request, 'core/nova_conta.html', contexto)
    else:
        usuario_logado = get_object_or_404(User, pk=request.user.id)
        form = ContaForm(data=request.POST)
        if form.is_valid():
            conta = form.save(commit=False)
            conta.usuario = usuario_logado
            conta.save()

            return redirect('contas')

    #     descricao = request.POST['descricao']
    #     categoria = request.POST['categoria']
    #     valor = request.POST['valor']
    #     data = request.POST['data']
    #     tipo = request.POST['tipo']
    #
    #     usuario_logado = get_object_or_404(User, pk=request.user.id)
    #
    #     print(descricao, categoria, valor, data, tipo, usuario_logado)
    #
    #     categoria = Categoria.objects.get(id=categoria)
    #
    #     conta = Conta.objects.create(descricao=descricao, valor=valor,
    #                                  tipo=tipo, categoria=categoria,
    #                                  data=data, usuario=usuario_logado)
    #     conta.save()
    #
    #     return redirect('contas')
    #
    # categorias = Categoria.objects.filter(usuario=request.user.id)
    #
    # context = {
    #     'categorias': categorias
    # }
    # return render(request, 'core/nova_conta.html', context)


@login_required(login_url='login')
def contas(request):
    contas = Conta.objects.filter(usuario=1).order_by('data_add').reverse()
    context = {
        'contas': contas
    }
    return render(request, 'core/contas.html', context)


@login_required(login_url='login')
def editar_conta(request, id):
    conta = Conta.objects.get(id=id)

    if request.method == 'GET':
        form = ContaForm(instance=conta)
        contexto = {'form': form, 'conta': conta}
        return render(request, 'core/editar_conta.html', contexto)

    else:
        form = ContaForm(instance=conta, data=request.POST)
        if form.is_valid():
            form.save()

            return redirect('contas')

    # if request.method == 'GET':
    #     categorias = Categoria.objects.all()
    #     conta = Conta.objects.get(id=id)
    #     print(conta.descricao, conta.valor, conta.data)
    #     context = {
    #         'conta': conta,
    #         'categorias': categorias
    #     }
    #
    #     return render(request, 'core/editar_conta.html', context)
    #
    # else:
    #     descricao = request.POST['descricao']
    #     categoria = request.POST['categoria']
    #     valor = request.POST['valor']
    #     data = request.POST['data']
    #     tipo = request.POST['tipo']
    #
    #     print(valor, data)
    #
    #     # usuario_logado = get_object_or_404(User, pk=request.user.id)
    #
    #     Conta.objects.filter(id=id).update(descricao=descricao,
    #                                        valor=valor, tipo=tipo,
    #                                        categoria=categoria,
    #                                        data=data)
    #
    #     return redirect('contas')


@login_required(login_url='login')
def deletar_conta(request, id):
    conta = Conta.objects.get(id=id)
    conta.delete()
    return redirect('contas')


@login_required(login_url='login')
def categoria(request):
    if request.method == 'POST':
        # descricao = request.POST['descricao']
        # print(descricao)
        usuario_logado = get_object_or_404(User, pk=request.user.id)
        # nova_categoria = Categoria.objects.create(descricao=descricao,
        #                                           usuario=usuario_logado)
        # nova_categoria.save()

        form = CategoriaForm(request.POST)

        if form.is_valid():
            categoria = form.save(commit=False)
            categoria.usuario = usuario_logado
            categoria.save()

            return redirect('categorias')

    else:
        form = CategoriaForm()
        contexto = {'form': form}

        return render(request, 'core/nova_categoria.html', contexto)


@login_required(login_url='login')
def categorias(request):
    categorias = Categoria.objects.filter(usuario=request.user.id)

    context = {
        'categorias': categorias,
    }

    return render(request, 'core/categorias.html', context)


@login_required(login_url='login')
def editar_categoria(request, id):
    # if request.method == 'GET':
    #     categoria = Categoria.objects.get(id=id)
    #     context = {
    #         'categoria': categoria
    #     }
    #
    #     return render(request, 'core/editar_categoria.html', context)
    #
    # else:
    #     descricao = request.POST['descricao']
    #
    #
    #
    #     Categoria.objects.filter(id=id).update(descricao=descricao)
    #
    #     return redirect('categorias')

    categoria = Categoria.objects.get(id=id)

    if request.method == 'GET':
        form = CategoriaForm(instance=categoria)
        contexto = {'form': form, 'categoria': categoria}

        return render(request, 'core/editar_categoria.html', contexto)

    else:
        form = CategoriaForm(instance=categoria, data=request.POST)
        if form.is_valid():
            form.save()

        return redirect('categorias')


@login_required(login_url='login')
def deletar_categoria(request, id):
    categoria = Categoria.objects.get(id=id)
    categoria.delete()
    return redirect('categorias')
