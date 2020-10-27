from limite.tela_cliente import TelaCliente
from entidade.cliente import Cliente
import sys


class ControladorCliente:
    def __init__ (self):
        self.__tela_cliente = TelaCliente(self)
        self.__clientes = []

    def inicia (self):
        self.abre_tela_inicial()
    
    def entrar (self):
        self.__tela_cliente.tela_cliente()

    def voltar (self):
        print("bobi")
        sys.exit(0)

    def cadastrar (self):
        dados = self.__tela_cliente.tela_cadastro()
        novo_cliente = Cliente(dados[0], dados[1], dados[2])
        self.__clientes.append(novo_cliente)

    def abre_tela_inicial(self):
        switcher = {1: self.entrar, 2: self.cadastrar, 3: self.voltar}

        while True:
            opcao  = self.__tela_cliente.mostra_tela_opcoes()
            funcao_escolhida = switcher[opcao]
            funcao_escolhida()
