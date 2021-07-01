from django.contrib.auth.models import User
from django.db import models
# from auditlog.registry import auditlog


class Categoria(models.Model):
    descricao = models.CharField('descrição', max_length=30)
    TIPO = [('P', 'Pagar'), ('R', 'Receber')]
    tipo = models.CharField(choices=TIPO, max_length=1)
    ativa = models.BooleanField(default=True, verbose_name='Ativa')
    data_add = models.DateField('Data cadastro', auto_now_add=True)
    usuario = models.ForeignKey(User, on_delete=models.PROTECT,
                                verbose_name='Dono')

    def __str__(self):
        return self.descricao

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'


class Orcamento(models.Model):
    descricao = models.CharField('descrição', max_length=30)
    atual = models.BooleanField('atual')
    data_add = models.DateField('Data cadastro', auto_now_add=True)
    usuario = models.ForeignKey(User, on_delete=models.PROTECT,
                                verbose_name='Dono')

    def __str__(self):
        return self.descricao

    class Meta:
        verbose_name = 'Orçamento'
        verbose_name_plural = 'Orçamentos'


class ValorOrcamentario(models.Model):
    orcamento = models.ForeignKey(Orcamento, on_delete=models.PROTECT)
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT,
                                  related_name='valor_categoria')
    valor_total = models.DecimalField('Valor total', max_digits=10,
                                      decimal_places=2)
    valor_disponivel = models.DecimalField('Valor disponível', null=True,
                                           blank=True, max_digits=10,
                                           decimal_places=2)

    def __str__(self):
        return self.categoria.descricao

    class Meta:
        verbose_name = 'Valor Orçamentário'
        verbose_name_plural = 'Valores Orçamentários'


class Conta(models.Model):
    descricao = models.CharField('descrição', max_length=40, null=False)
    valor = models.DecimalField('valor', max_digits=10, decimal_places=2,
                                null=False)
    TIPO = [('P', 'Pagar'), ('R', 'Receber')]
    tipo = models.CharField(choices=TIPO, max_length=1)
    prazo = models.BooleanField('prazo', default=False)
    quantidade_parcelas = models.IntegerField('quantidade de parcelas',
                                              max_length=2)
    data = models.DateField(null=False)
    data_add = models.DateField('Data cadastro', auto_now_add=True)
    usuario = models.ForeignKey(User, on_delete=models.PROTECT,
                                verbose_name='Dono')

    def __str__(self):
        return self.descricao

    class Meta:
        verbose_name = 'Conta'
        verbose_name_plural = 'Contas'


class Parcela(models.Model):
    conta = models.ForeignKey(Conta, on_delete=models.PROTECT,
                              verbose_name='conta')
    valor = models.DecimalField('valor', max_digits=10, decimal_places=2)
    vencimento = models.DateField('vencimento')
    pago = models.BooleanField('pago', default=False)
    data_add = models.DateField('Data cadastro', auto_now_add=True)
    usuario = models.ForeignKey(User, on_delete=models.PROTECT,
                                verbose_name='Dono')

    class Meta:
        verbose_name = 'Parcela'
        verbose_name_plural = 'Parcelas'

    def __str__(self):
        return self.conta.descricao


class Movimentacao(models.Model):
    parcela = models.OneToOneField(Parcela, on_delete=models.PROTECT,
                                   verbose_name='Parcela', blank=True,
                                   null=True)
    descricao = models.CharField('Descrição', max_length=40, null=False)
    valor = models.DecimalField('valor', max_digits=10, decimal_places=2,
                                null=False)
    TIPO = [('P', 'Pagar'), ('R', 'Receber')]
    tipo = models.CharField(choices=TIPO, max_length=1)
    data = models.DateField(null=False)
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT,
                                  verbose_name='Categoria')
    data_add = models.DateField('Data cadastro', auto_now_add=True)
    usuario = models.ForeignKey(User, on_delete=models.PROTECT,
                                verbose_name='Dono')

    def __str__(self):
        return self.descricao

    class Meta:
        verbose_name = 'Movimentação'
        verbose_name_plural = 'Movimentações'

# auditlog.register(Movimentacao)
# auditlog.register(Parcela)
# auditlog.register(Conta)
# auditlog.register(Orcamento)
# auditlog.register(ValorOrcamentario)
# auditlog.register(Categoria)
