from dao.abstract_dao import AbstractDao
from entidade.produto import Produto

class ProdutoDao(AbstractDao):
    def __init__(self):
        super().__init__('produtos.pkl')

    def add(self, produto: Produto):
        if isinstance(produto.nome, str) and isinstance(produto.preco, float) and isinstance(produto.estoque, int):
            super().add(produto.nome, produto)

    def get_all(self):
        return super().get_all()