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
