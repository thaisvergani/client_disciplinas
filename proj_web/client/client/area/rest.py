import requests
from ..base import BaseClient


class RestClient(BaseClient):
    def __init__(self, base_url="http://localhost:8080/universidade/rest/areas/"):
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

    def delete(self, content):
        response = requests.delete(self.base_url + str(content.get('id')))
        return response
