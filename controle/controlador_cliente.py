from limite.tela_cliente import TelaCliente
from entidade.cliente import Cliente
from entidade.produto import Produto
from controle.controlador_adm import ControladorAdm
from dao.cliente_dao import ClienteDao
from dao.produto_dao import ProdutoDao
import sys


class ControladorCliente:
    def __init__ (self, adm):
        self.__cliente_dao = ClienteDao()
        self.__tela_cliente = TelaCliente(self)
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
                    switcher = {1: self.ver_lista_de_produtos, 2: self.ver_carrinho, 3: self.remover_do_carrinho, 4: self.limpar_carrinho, 5: self.finalizar_compra, 0: None}

                    while True:
                        opcao = self.__tela_cliente.tela_cliente(cliente.nome)
                        if opcao == 0:
                            return switcher[opcao]

                        funcao_escolhida = switcher[opcao]
                        funcao_escolhida(cliente)
                else:
                    self.__tela_cliente.tela_erro()

    def verifica_entrada (self, nome, senha):
        print(self.__cliente_dao.get_all())
        for cliente in self.__cliente_dao.get_all():
            if ((cliente.nome == nome) or (cliente.cpf == nome)) and (cliente.senha == senha):
                return cliente
        return None

    def ver_carrinho (self, cliente):
        while True:
            opcao = self.__tela_cliente.tela_ver_produtos(cliente.carrinho())
            if opcao == 0:
                return None

    def ver_lista_de_produtos (self, cliente):
        while True:
            opcao = self.__tela_cliente.tela_ver_produtos(self.__adm.controlador_produto.produtos)
            if opcao == 0:
                return None
            else:
                self.coloca_no_carrinho(cliente, opcao)
        
    def coloca_no_carrinho (self, cliente, produto):
        cliente.carrinho().append(produto)
        while True:
            opcao = self.__tela_cliente.tela_adicionado_ao_carrinho()
            if opcao == 0:
                return None

    def remover_do_carrinho (self, cliente):
        while True:
            opcao = self.__tela_cliente.remcarrinho(cliente.carrinho())
            if opcao == None:
                return None
            else:
                cliente.remove_do_carrinho(opcao)

    def limpar_carrinho (self, cliente):
        opcao = self.__tela_cliente.limpar_carrinho()
        if opcao:
            cliente.limpa_carrinho()
            self.__tela_cliente.limpar_sucesso()
            return None
        else:
            return None

    def finalizar_compra (self, cliente):
        valor_da_compra = 0
        desconto = 0
        for item in cliente.carrinho():
            valor_da_compra += item.preco
        opcao = self.__tela_cliente.comprar(valor_da_compra)
        if opcao:
            for item in cliente.carrinho():
                if item.estoque > 0:
                    novo_estoque = item.estoque - 1
                    if item not in self.__adm.controlador_registro.produtos_excluidos():
                        produto_dao = self.__adm.controlador_produto.produtoDao()
                        produto_antigo_estoque = produto_dao.get(item.nome)
                        produto_alterado = Produto(produto_antigo_estoque.nome, produto_antigo_estoque.preco, novo_estoque)
                        produto_dao.remove(produto_antigo_estoque.nome)
                        produto_dao.add(produto_alterado)
                    else:
                        desconto += item.preco
                        print("Sem estoque de {}".format(item.nome))
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

    @property
    def clientes (self):
        return self.__cliente_dao.get_all()

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
                print(novo_cliente)
                self.__cliente_dao.add(novo_cliente)
                print(self.__cliente_dao.get_all())
                self.__tela_cliente.cadastro_sucesso()
                return None
        
    def existe (self, novo_cliente):
        for cliente in self.__cliente_dao.get_all():
            if cliente.nome == novo_cliente.nome:
                return self.__tela_cliente.fracasso_nome()
            if cliente.cpf == novo_cliente.cpf:
                return self.__tela_cliente.fracasso_cpf()
        return False

    def abre_tela_cliente(self):
        switcher = {1: self.entrar, 2: self.cadastrar, 0: self.voltar}

        while True:
            opcao  = self.__tela_cliente.mostra_tela_opcoes()
            funcao_escolhida = switcher[opcao]
            if funcao_escolhida() == "fim":
                return None
             
