from limite.tela_registro import TelaRegistro
import sys

class ControladorRegistro:

    def __init__(self, adm):
        self.__adm = adm
        self.__tela_registro = TelaRegistro(self)
        self.__lista_produtos_incluidos = []
        self.__lista_produtos_excluidos = []
        self.__lista_produtos_alterados = []
        self.__lista_clientes_incluidos = []
        self.__produto_mais_caro = None
        self.__produto_mais_barato = None

    def inicia(self):
        self.abre_tela_registro()

    def voltar(self):
        return "fim"

    def cliente_foi_incluido (self, cliente):
        self.__lista_clientes_incluidos.append(cliente)

    def lista_clientes_incluidos(self):
        while True:
            opcao = self.__tela_registro.tela_ver_clientes_incluidos(self.__lista_clientes_incluidos)
            if opcao == 0:
                return None  

    def produto_foi_incluido (self, produto):
        self.__lista_produtos_incluidos.append(produto)

    def lista_produtos_incluidos(self):
        while True:
            opcao = self.__tela_registro.tela_ver_incluidos(self.__lista_produtos_incluidos)
            if opcao == 0:
                return None  

    def produto_foi_excluido (self, produto):
        self.__lista_produtos_excluidos.append(produto)

    def lista_produtos_excluidos(self):
        while True:
            opcao = self.__tela_registro.tela_ver_excluidos(self.__lista_produtos_excluidos)
            if opcao == 0:
                return None 

    def produto_foi_alterado (self, produto):
        self.__lista_produtos_alterados.append(produto)

    def lista_produtos_alterados(self):
        while True:
            opcao = self.__tela_registro.tela_ver_alterados(self.__lista_produtos_alterados)
            if opcao == 0:
                return None

    def produto_mais_caro(self):
        for produto in self.__adm.controlador_produto.produtos():
            if self.__produto_mais_caro == None:
                self.__produto_mais_caro = produto
            else:
                if produto.preco > self.__produto_mais_caro.preco:
                    self.__produto_mais_caro = produto

        while True:
            opcao = self.__tela_registro.tela_ver_mais_caro(self.__produto_mais_caro)
            if opcao == 0:
                return None

    def produto_mais_barato(self):
        for produto in self.__adm.controlador_produto.produtos():
            if self.__produto_mais_barato == None:
                self.__produto_mais_barato = produto
            else:
                if produto.preco < self.__produto_mais_barato.preco:
                    self.__produto_mais_barato = produto

        while True:
            opcao = self.__tela_registro.tela_ver_mais_barato(self.__produto_mais_barato)
            if opcao == 0:
                return None
         
    def abre_tela_registro(self):
        switcher = {1: self.lista_produtos_incluidos, 2: self.lista_produtos_excluidos, 3: self.lista_produtos_alterados, 4: self.produto_mais_caro, 5: self.produto_mais_barato, 6: self.lista_clientes_incluidos, 0: self.voltar}
        while True:
            opcao = self.__tela_registro.mostra_opcoes()
            funcao_escolhida = switcher[opcao]
            if funcao_escolhida() == "fim":
                return None       