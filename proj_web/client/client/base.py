import abc


class BaseClient(object):
    __metaclass__ = abc.ABCMeta

    def post(self, content):
        pass

    def put(self, pk, content):
        pass

    def get(self, pk=''):
        pass

    def delete(self, content):
        pass