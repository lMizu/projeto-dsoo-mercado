from limite.tela_inicial import TelaInicial
from controle.controlador_cliente import ControladorCliente
from controle.controlador_adm import ControladorAdm
import sys

class ControladorTela:
    def __init__ (self):
        self.__tela_inicial = TelaInicial(self)

    def inicia (self):
        self.abre_tela_inicial()

    def abre_tela_inicial(self):
        switcher = {1: self.entrar_como_cliente, 2: self.entrar_como_adm, 0: self.fechar}

        while True:
            opcao  = self.__tela_inicial.mostra_tela_opcoes()
            funcao_escolhida = switcher[opcao]
            funcao_escolhida()

    def entrar_como_cliente (self):
        ControladorCliente().inicia()

    def entrar_como_adm (self):
        ControladorAdm().inicia()

    def fechar (self):
        print("Esperamos te ver novamente em breve! <3")
        sys.exit(0)
