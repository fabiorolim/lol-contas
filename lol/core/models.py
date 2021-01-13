from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class Categoria(models.Model):
    descricao = models.CharField(max_length=30, null=False,
                                 verbose_name='Descrição')
    ativa = models.BooleanField(default=True, verbose_name='Ativa')
    data_add = models.DateField(auto_now_add=True, verbose_name='Data cadastro')
    usuario = models.ForeignKey(User, on_delete=models.PROTECT,
                                related_name='Criador', verbose_name='Dono')

    def __str__(self):
        return self.descricao

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'


class Conta(models.Model):
    descricao = models.CharField(max_length=40, null=False,
                                 verbose_name='Descrição')
    valor = models.DecimalField(max_digits=10, decimal_places=2, null=False,
                                verbose_name='Valor')
    # tipo = models.CharField(max_length=1, null=False, verbose_name='Tipo')
    TIPO = [('P', 'Pagar'), ('R', 'Receber')]
    tipo = models.CharField(choices=TIPO, max_length=1)
    data_add = models.DateField(auto_now_add=True, verbose_name='Data cadastro')
    data = models.DateField(null=False)
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT,
                                  related_name='Categoria',
                                  verbose_name='Categoria')
    usuario = models.ForeignKey(User, on_delete=models.PROTECT,
                                related_name='Dono', verbose_name='Dono')

    def __str__(self):
        return self.descricao

    class Meta:
        verbose_name = 'Conta'
        verbose_name_plural = 'Contas'
