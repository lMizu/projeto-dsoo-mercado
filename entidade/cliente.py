class Cliente:
    def __init__ (self, nome: str, senha: str, cpf: str):
        if isinstance (nome, str):
            self.__nome = nome

        if isinstance (senha, str):
            self.__senha = senha

        if isinstance (cpf, str):
            self.__cpf = cpf

        self.__carrinho = []
 
    @property
    def nome (self):
        return self.__nome

    @nome.setter
    def nome (self, nome):
        self.__nome = nome

    @property
    def senha (self):
        return self.__senha

    @senha.setter
    def senha (self, senha):
        self.__senha = senha

    @property
    def cpf (self):
        return self.__cpf

    @cpf.setter
    def cpf (self, cpf):
        self.__cpf = cpf

    def carrinho (self):
        return self.__carrinho