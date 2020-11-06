from limite.tela_cliente import TelaCliente
from entidade.cliente import Cliente
from entidade.produto import Produto
from controle.controlador_adm import ControladorAdm
import sys


class ControladorCliente:
    def __init__ (self, adm):
        self.__tela_cliente = TelaCliente(self)
        self.__clientes = [Cliente("Teste", "a", "a")]
        self.__adm = adm

    def inicia (self):
        self.abre_tela_cliente()
    
    def entrar (self):
        while True:    
            inputs = self.__tela_cliente.tela_login_cliente()
            if inputs == None:
                return None
            else:
                cliente = self.verifica_entrada(inputs[0], inputs[1])
                if cliente != None:
                    print("--------------------------")
                    print("Prazer {}".format(cliente.nome))
                    print("")
                    switcher = {1: self.ver_lista_de_produtos, 2: self.ver_carrinho, 3: self.remover_do_carrinho, 4: self.limpar_carrinho, 5: self.finalizar_compra, 0: None}

                    while True:
                        opcao = self.__tela_cliente.tela_cliente()
                        if opcao == 0:
                            return switcher[opcao]

                        funcao_escolhida = switcher[opcao]
                        funcao_escolhida(cliente)
                else:
                    print("dados incorretos")

    def verifica_entrada (self, nome, senha):
        for cliente in self.clientes():
            if ((cliente.nome == nome) or (cliente.cpf == nome)) and (cliente.senha == senha):
                return cliente
        return None

    def ver_carrinho (self, cliente):
        print("----------------------------")
        i = 1
        if len(cliente.carrinho()) == 0:
            print("CARRINHO VAZIO")
        for item in cliente.carrinho():
            print("{} - {}".format(i, item.nome))
            i += 1
        print("----------------------------")

    def ver_lista_de_produtos (self, cliente):
        while True:    
            self.__adm.controlador_produto.lista_produtos()
            lista = self.__adm.controlador_produto.produtos()
            opcao = self.__tela_cliente.colocar_item_no_carrinho(lista)

            if opcao == None:
                return None
            self.coloca_no_carrinho(cliente, opcao)
        
    def coloca_no_carrinho (self, cliente, opcao):
        cliente.carrinho().append(self.__adm.controlador_produto.produtos()[opcao - 1])
        self.__tela_cliente.tela_add_ao_carrinho()

    def remover_do_carrinho (self, cliente):
        while True:
            self.ver_carrinho(cliente)
            print("0 - VOLTAR")
            opcao = self.__tela_cliente.remove_do_carrinho(cliente.carrinho())
            if opcao == None:
                return None
            cliente.remove_do_carrinho(opcao)

    def limpar_carrinho (self, cliente):
        opcao = self.__tela_cliente.limpar_carrinho()
        if opcao:
            cliente.limpa_carrinho()
            print("CARRINHO LIMPO")
            print("----------------------------------------")
            return None
        else:
            return None

    def finalizar_compra (self, cliente):
        self.ver_carrinho(cliente)
        valor_da_compra = 0
        desconto = 0
        for item in cliente.carrinho():
            valor_da_compra += item.preco
        opcao = self.__tela_cliente.comprar(valor_da_compra)
        if opcao:
            for item in cliente.carrinho():
                if item.estoque > 0:
                    novo_estoque = item.estoque - 1
                    posicao = self.__adm.controlador_produto.produtos().index(item)
                    self.__adm.controlador_produto.produtos()[posicao].estoque = novo_estoque
                else:
                    desconto += item.preco
                    print("Sem estoque de {}".format(item.nome))
            if desconto == 0:
                self.__tela_cliente.pagamento(desconto)
                cliente.limpa_carrinho()
                return None
            else:
                self.__tela_cliente.pagamento(desconto)
                cliente.limpa_carrinho()
                return None
        else:
            return None

    def clientes (self):
        return self.__clientes

    def voltar (self):
        return "fim"

    def cadastrar (self):
        while True:
            dados = self.__tela_cliente.tela_cadastro()
            if dados != None:
                novo_cliente = Cliente(dados[0], dados[1], dados[2])
            else:
                return None
            verificacao = self.existe(novo_cliente)
            if verificacao == False:
                self.__adm.controlador_registro.cliente_foi_incluido(novo_cliente)
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

    def abre_tela_cliente(self):
        switcher = {1: self.entrar, 2: self.cadastrar, 0: self.voltar}

        while True:
            opcao  = self.__tela_cliente.mostra_tela_opcoes()
            funcao_escolhida = switcher[opcao]
            if funcao_escolhida() == "fim":
                return None
             
