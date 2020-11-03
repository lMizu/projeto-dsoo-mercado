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
        while True:
            opcao = self.__tela_produto.tela_ver_produto(self.__produtos)
            if opcao == 0:
                self.abre_tela_produto()

    def cadastra_produto(self):
        while True:
            dados = self.__tela_produto.tela_cadastra_produto()
            if dados != None:
                novo_produto = Produto(dados[0], dados[1], dados[2])
            else:
                self.abre_tela_produto()
            if self.existe(novo_produto):
                print("Um produto com este mesmo nome já foi cadastrado")
            else:
                self.__produtos.append(novo_produto)
                print("Produto cadastrado com sucesso")
                self.abre_tela_produto()

    def sair(self):
        sys.exit(0)

    def existe(self, novo_produto):
        for produto in self.__produtos:
            if produto.nome == novo_produto.nome:
                return True

    def abre_tela_produto(self):
        switcher = {1: self.lista_produtos, 2: self.cadastra_produto, 0: self.sair}
        while True:
            opcao = self.__tela_produto.mostra_opcoes()
            funcao_escolhida = switcher[opcao]
            funcao_escolhida()

