from zeep import Client, helpers as zeep_helper

from ..base import BaseClient
from ..area.soap import SoapClient as AreaSoapClient
from ..courses.soap import SoapClient as CoursesSoapClient

AREAS_CLIENT = AreaSoapClient
COURSES_CLIENT = CoursesSoapClient


class SoapClient(BaseClient):
    def __init__(self, base_url="http://localhost:8080/universidade/disciplinas?wsdl"):
        self.base_url = base_url
        self.client = Client(
            self.base_url
        )

    def post(self, content):

        response = self.client.service.insere(content)
        return zeep_helper.serialize_object(response)

    def put(self, pk, content):

        content['id'] = pk
        response = self.client.service.altera(content)
        return zeep_helper.serialize_object(response)

    def get(self, pk=''):

        if pk:
            response = self.client.service.buscaPorId(pk)
        else:
            response = self.client.service.buscaTodos()

        return zeep_helper.serialize_object(response)

    def delete(self, content):
        response = self.client.service.remove(content)
        return zeep_helper.serialize_object(response)
