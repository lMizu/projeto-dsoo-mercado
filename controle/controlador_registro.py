from limite.tela_registro import TelaRegistro
from entidade.registro import Registro
import sys

class ControladorRegistro:

    def __init__(self):
        self.__tela_registro = TelaRegistro(self)
        self.__lista_incluidos = []
        self.__lista_excluidos = []
        self.__lista_alterados = []
        self.__mais_caro = None
        self.__mais_barato = None

    def inicia(self):
        self.abre_tela_registro

    def sair(self):
        sys.exit(0)

    def lista_incluidos(self):
        while True:
            opcao = self.__tela_registro.tela_ver_incluidos(self.__lista_incluidos)
            if opcao == 0:
                return None  

    def lista_excluidos(self):
        while True:
            opcao = self.__tela_registro.tela_ver_excluidos(self.__lista_excluidos)
            if opcao == 0:
                return None 

    def lista_alterados(self):
        while True:
            opcao = self.__tela_registro.tela_ver_alterados(self.__lista_alterados)
            if opcao == 0:
                return None

    def mais_caro(self):
        while True:
            opcao = self.__tela_registro.tela_ver_mais_caro(self.__mais_caro)
            if opcao == 0:
                return None

    def mais_barato(self):
        while True:
            opcao = self.__tela_registro.tela_ver_mais_barato(self.__mais_barato)
            if opcao == 0:
                return None
         
    def abre_tela_registro(self):
        switcher = {1: self.lista_incluidos, 2: self.lista_excluidos, 3: self.lista_alterados, 4: self.mais_caro, 5: self.mais_barato, 0: self.sair}
        while True:
            opcao = self.__tela_registro.mostra_opcoes()
            funcao_escolhida = switcher[opcao]
            funcao_escolhida()        