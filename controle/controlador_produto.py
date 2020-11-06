from limite.tela_produto import TelaProduto
from entidade.produto import Produto
import sys

class ControladorProduto:
    def __init__(self, adm):
        self.__adm = adm
        self.__tela_produto = TelaProduto(self)
        self.__produtos = [Produto("Uva", 10.0, 4), Produto("Laranja", 5.0, 2)]

    def produtos (self):
        return self.__produtos

    def inicia(self):
        self.abre_tela_produto()

    def lista_produtos(self):
        return self.__tela_produto.tela_ver_produto(self.__produtos)

    def cadastra_produto(self):
        while True:
            dados = self.__tela_produto.tela_cadastra_produto()
            if dados != None:
                novo_produto = Produto(dados[0], dados[1], dados[2])
            else:
                return None
            if self.existe(novo_produto):
                print("Um produto com este mesmo nome já foi cadastrado")
            else:
                self.__adm.controlador_registro.produto_foi_incluido(novo_produto)
                self.__produtos.append(novo_produto)
                print("Produto cadastrado com sucesso")
                return None
            
    def altera_produto(self):
        while True:
            dados = self.__tela_produto.tela_altera_produto(self.__produtos)
            if dados != None:
                for produto in self.__produtos:
                    if produto == dados[0]:
                        produto_velho = Produto(produto.nome, produto.preco, produto.estoque)
                        self.__adm.controlador_registro.produto_foi_alterado(produto_velho)
                        produto.nome = dados[1]
                        produto.preco = dados[2]
                        produto.estoque = dados[3]
            else:
                return None

    def deleta_produto (self):
        while True:
            dados = self.__tela_produto.tela_deleta_produto(self.__produtos)
            if dados != None:
                for produto in self.__produtos:
                    if produto == dados[0]:
                        self.__adm.controlador_registro.produto_foi_excluido(produto)
                        self.__produtos.remove(produto)
            else: 
                return None

    def sair (self):
        return "fim"

    def existe(self, novo_produto):
        for produto in self.__produtos:
            if produto.nome == novo_produto.nome:
                return True

    def abre_tela_produto (self):
        switcher = {1: self.lista_produtos, 2: self.cadastra_produto, 3: self.altera_produto, 4: self.deleta_produto, 0: self.sair}
        while True:
            opcao = self.__tela_produto.mostra_opcoes()
            funcao_escolhida = switcher[opcao]
            if funcao_escolhida() == "fim":
                return None

