from limite.tela_produto import TelaProduto
from entidade.produto import Produto
from dao.produto_dao import ProdutoDao
import sys


class ControladorProduto:
    def __init__(self, adm):
        self.__adm = adm
        self.__tela_produto = TelaProduto(self)
        self.__produtos = []

    def produtos(self):
        return self.__produtos

    def inicia(self):
        self.abre_tela_produto()

    def lista_produtos(self):
        while True:
            opcao = self.__tela_produto.tela_ver_produtos(
                self.__produtos)
            if opcao == 0:
                return None
            else:
                self.edita_produto(opcao)

    def cadastra_produto(self):
        while True:
            dados = self.__tela_produto.tela_cadastra_produto()
            if dados != None:
                novo_produto = Produto(dados[0], dados[1], dados[2])
                if self.existe(novo_produto):
                    #Adicionar dialog
                    return None
                else:
                    self.__adm.controlador_registro.produto_foi_incluido(
                        novo_produto)
                    self.__produtos.append(novo_produto)
                    return None
            else:
                return None

    def edita_produto(self, produto):
        while True:
            dados = self.__tela_produto.tela_edita_produto(produto)
            if dados == 0 or dados == None:
                return None
            elif dados == 1:
                self.__produtos.remove(produto)
                self.__adm.controlador_registro.produto_foi_excluido(produto)
                return None
            else:
                produto_velho = Produto(
                    produto.nome, produto.preco, produto.estoque)
                self.__adm.controlador_registro.produto_foi_alterado(
                    produto_velho)
                produto.nome = dados[0]
                produto.preco = dados[1]
                produto.estoque = dados[2]

    def sair(self):
        return "fim"

    def existe(self, novo_produto):
        for produto in self.__produtos:
            if produto.nome == novo_produto.nome:
                return True

    def abre_tela_produto(self):
        switcher = {1: self.lista_produtos,
                    2: self.cadastra_produto, 0: self.sair}
        while True:
            opcao = self.__tela_produto.mostra_opcoes()
            funcao_escolhida = switcher[opcao]
            if funcao_escolhida() == "fim":
                return None
