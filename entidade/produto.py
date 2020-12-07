class Produto:

    def __init__(self, nome: str, preco: float, estoque: int):
        if isinstance(nome, str):
            self.__nome = nome
        if isinstance(preco, float):
            self.__preco = preco
        if isinstance(estoque, int):
            self.__estoque = estoque

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome: str):
        if isinstance(nome, str):
            self.__nome = nome

    def nome1(self):
        return self.__nome

    @property
    def preco(self):
        return self.__preco

    @preco.setter
    def preco(self, preco: float):
        if isinstance(preco, float):
            self.__preco = preco

    @property
    def estoque(self):
        return self.__estoque

    @estoque.setter
    def estoque(self, estoque: int):
        if isinstance(estoque, int):
            self.__estoque = estoque
