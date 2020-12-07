from dao.abstract_dao import AbstractDao
from entidade.cliente import Cliente

class ClienteDao(AbstractDao):
    def __init__(self):
        super().__init__('clientes.pkl')

    def add (self, cliente: Cliente):
        super().add(cliente.nome, cliente)

    def get (self, key: int):
        if isinstance(key, int):
            return super().get(key)

    def remove (self, key: int):
        if isinstance(key, int):
            return super().remove(key)

    def get_all(self):
        return super().get_all()