from limite.tela_produto import TelaProduto
from entidade.produto import Produto
import sys

class ControladorProduto:

    def __init__(self):
        self.__tela_produto = TelaProduto(self)
        self.__produtos = []

    def inicia(self):
        self.abre_tela_produto()

    def lista_produtos(self):
        pass

    def cadastra_produto(self):
        pass

    def sair(self):
        sys.exit(0)

    def abre_tela_produto(self):
        switcher = {1: self.lista_produtos, 2: self.cadastra_produto, 0: self.sair}
        while True:
            opcao = self.__tela_produto.mostra_opcoes()
            funcao_escolhida = switcher[opcao]
            funcao_escolhida()

