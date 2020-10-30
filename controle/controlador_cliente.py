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
        while True:    
            inputs = self.__tela_cliente.tela_login_cliente()
            if inputs == None:
                return None
            else:
                valores = self.verifica_entrada(inputs[0], inputs[1])
                if valores != None:
                    print("--------------------------")
                    print("Bem vindo {}".format(valores.nome))
                    print("")
                    switcher = {1: valores.carrinho, 2: self.finalizar_compra, 3: None}

                    while True:
                        opcao = self.__tela_cliente.tela_cliente()
                        if opcao == 3:
                            return switcher[opcao]
                        funcao_escolhida = switcher[opcao]
                        funcao_escolhida()
                else:
                    print("dados incorretos")

    def verifica_entrada (self, nome, senha):
        for cliente in self.clientes():
            if ((cliente.nome or cliente.cpf) == nome) and (cliente.senha == senha):
                return cliente
        return None

    def finalizar_compra (self):
        pass 

    def sair (self):
        pass

    def clientes (self):
        return self.__clientes

    def voltar (self):
        print("bobi")
        sys.exit(0)

    def cadastrar (self):
        while True:
            dados = self.__tela_cliente.tela_cadastro()
            if dados != None:
                novo_cliente = Cliente(dados[0], dados[1], dados[2])
            else:
                return None
            verificacao = self.existe(novo_cliente)
            if verificacao == False:
                self.__clientes.append(novo_cliente)
                print("cadastrado com sucesso")
                return None
            else:
                print(verificacao)
                print("Informe dados validos")
        

    def existe (self, novo_cliente):
        for cliente in self.__clientes:
            if cliente.nome == novo_cliente.nome:
                return "Este nome ja foi escolhido"
            if cliente.cpf == novo_cliente.cpf:
                return "Este cpf ja foi escolhido"
        return False


    def abre_tela_inicial(self):
        switcher = {1: self.entrar, 2: self.cadastrar, 3: self.voltar}

        while True:
            opcao  = self.__tela_cliente.mostra_tela_opcoes()
            funcao_escolhida = switcher[opcao]
            funcao_escolhida()
