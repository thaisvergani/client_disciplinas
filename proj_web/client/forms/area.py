from django import forms


class AreaForm(forms.Form):
    nome = forms.CharField(max_length=30)
    sigla = forms.CharField(max_length=30)
