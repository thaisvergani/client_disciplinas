import requests
from django import forms


class RestClient(object):
    def __init__(self, base_url="http://localhost:8080/universidade/rest/cursos/"):
        self.base_url = base_url

    def post(self, content):
        response = requests.post(self.base_url, json=content)
        return response

    def put(self, pk, content):
        response = requests.put(self.base_url + pk, json=content)
        return response

    def get(self, pk=''):
        response = requests.get(self.base_url + pk)
        return response.json()

    def delete(self, pk=None):
        response = requests.delete(self.base_url + pk)
        return response


class CursoForm(forms.Form):
    nome = forms.CharField(max_length=30)
    codigo = forms.IntegerField()


class DisciplinaForm(forms.Form, RestClient):
    nome = forms.CharField(max_length=30)
    codigo = forms.EmailField(max_length=254)
    curso = forms.ChoiceField()
    area = forms.ChoiceField()
    cargaHoraria = forms.IntegerField()


class AreaForm(forms.Form, RestClient):
    nome = forms.CharField(max_length=30)
    sigla = forms.CharField(max_length=30)
