from dao.abstract_dao import AbstractDao
from entidade.produto import Produto

class ProdutoDao(AbstractDao):
    def __init__(self):
        super().__init__('produtos.pkl')

    def add(self, produto: Produto):
        super().add(produto.nome, produto)

    def get_all(self):
        return super().get_all()

    def get (self, key: str):
        if isinstance(key, str):
            return super().get(key)

    def remove (self, key: str):
        if isinstance(key, str):
            return super().remove(key)