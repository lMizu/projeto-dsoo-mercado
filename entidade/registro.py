class Registro:

    def __init__(self, nome_produto, preco_produto, responsavel):
        if isinstance(nome_produto, str):
            self.__nome_produto = nome_produto
        if isinstance(preco_produto, float):
            self.__preco_produto = preco_produto
        if isinstance(responsavel, str):
            self.__responsavel = responsavel

    @property
    def nome_produto(self):
        return self.__nome_produto
    
    @nome_produto.setter
    def nome_produto(self, nome_produto):
        if isinstance(nome_produto, str):
            self.__nome_produto = nome_produto

    @property
    def preco_produto(self):
        return self.__preco_produto

    @preco_produto.setter
    def preco_produto(self, preco_produto):
        if isinstance(preco_produto, float):
            self.__preco_produto = preco_produto

    @property
    def responsavel(self):
        return self.__responsavel

    @responsavel.setter
    def responsavel(self, responsavel):
        if isinstance(responsavel, str):
            self.__responsavel = responsavel
            