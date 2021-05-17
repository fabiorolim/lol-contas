from django import forms

from lol.core.models import Conta, Categoria


class ContaForm(forms.ModelForm):
    class Meta:
        model = Conta
        fields = ['descricao', 'valor', 'tipo', 'categoria', 'data']
        widgets = {
            'descricao': forms.TextInput(
                attrs={'class': 'form-control form-control-user',
                       'placeholder': 'Descrição'}),
            'valor': forms.NumberInput(
                attrs={'class': 'form-control form-control-user',
                       'placeholder': 'Valor'}),
            'tipo': forms.Select(
                attrs={'class': 'form-control form-control-user',
                       'placeholder': 'Tipo'}),
            'categoria': forms.Select(
                attrs={'class': 'form-control form-control-user',
                       'placeholder': 'Categoria'}),
            'data': forms.DateInput(
                attrs={'class': 'form-control form-control-user',
                       'placeholder': 'Data dd/mm/yyyy'})
        }


class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['descricao']
        widgets = {'descricao': forms.TextInput(
            attrs={'class': 'form-control form-control-user',
                   'placeholder': 'Descrição'})}


class SimuladorForm(forms.Form):
    valor = forms.DecimalField(widget=forms.NumberInput(
        attrs={'class': 'form-control form-control-user',
               'placeholder': 'Valor R$'}))
    entrada = forms.DecimalField(widget=forms.NumberInput(
        attrs={'class': 'form-control form-control-user',
               'placeholder': 'Entrada R$'}))
    taxa = forms.DecimalField(widget=forms.NumberInput(
        attrs={'class': 'form-control form-control-user',
               'placeholder': 'Taxa a.m'}))
    prazo = forms.IntegerField(widget=forms.NumberInput(
        attrs={'class': 'form-control form-control-user',
               'placeholder': 'Prazo em meses'}))
    tipo = forms.CharField(widget=forms.Select(
        choices=(('P', 'Price'), ('S', 'SAC')),
        attrs={'class': 'form-control form-control-user',
               'placeholder': 'Tipo'}))
