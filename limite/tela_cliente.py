from limite.tela_le_inteiro import TelaLeInteiro


class TelaCliente(TelaLeInteiro):
    def __init__ (self, controlador):
        self.__controlador = controlador

    def mostra_tela_opcoes (self):
        print("--------------------------")
        print("ESCOLHA ENTRE 1 2 E 0 PARA NAVEGAR")
        print("1 - LOGAR")
        print("2 - CADASTRAR")
        print("0 - SAIR")
        print("--------------------------")
        opcao = self.le_inteiro("Escolha uma opcao: ", [1, 2, 0])
        return opcao

    def tela_login_cliente (self):
        print("----------------------------------------")
        nome = input(str("coloque seu nome de usuario ou cpf: "))
        senha = input(str("coloque sua senha: "))
        print("1 - ENTRA")
        print("0 - VOLTAR")
        print("----------------------------------------")
        opcao = self.le_inteiro("Escolha uma opcao: ", [1, 0])
        if opcao == 1:
            return [nome, senha]
        else:
            return None

    def tela_cliente (self):
        print("ESCOLHA ENTRE 1 2 3 4 5 E 0 PARA NAVEGAR")
        print("1 - VER PRODUTOS")
        print("2 - VER CARRINHO")
        print("3 - REMOVER PRODUTO DO CARRINHO")
        print("4 - LIMPAR CARRINHO")
        print("5 - FINALIZAR COMPRA")
        print("0 - SAIR")
        print("--------------------------")
        opcao = self.le_inteiro("Escolha uma opcao: ", [1, 2, 3, 4, 5, 0])
        return opcao

    def tela_cadastro (self):
        print("----------------------------------------")
        nome = input(str("coloque seu nome de usuario: "))
        cpf = input(str("coloque seu cpf: "))
        senha = self.senha_igual()
        print("----------------------------------------")
        print("1 - CONFIRMAR CADASTRO")
        print("0 - CANCELAR")
        print("----------------------------------------")
        opcao = self.le_inteiro("Escolha uma opcao: ", [1, 0])
        if opcao == 1:
            return [nome, cpf, senha]
        else:
            return None

    def senha_igual (self):
        while True:
            senha1 = input(str("coloque sua senha: "))
            senha2 = input(str("coloque sua senha novamente: "))
            try:
                if senha1 != senha2:
                    raise ValueError
                return senha1
            except ValueError:
                print("Valores discrepantes, coloque senhas iguais")

    def colocar_item_no_carrinho (self, lista_de_produtos):
        print("----------------------------")
        if len(lista_de_produtos) == 0:
                print("Não há produtos no mercado")
        else:
            print("ESCOLHA O PRODUTO QUE DESEJA ADICIONAR AO CARRINHO")
            posicao = 0
            produto_por_posicao = {}
            lista_opcoes = []
            for produto in lista_de_produtos:
                posicao += 1
                print("{} - {} / R${} / x{}".format(posicao, produto.nome, produto.preco, produto.estoque))
                produto_por_posicao[posicao] = produto
                lista_opcoes.append(posicao)
            lista_opcoes.append(0)
            print("0 - VOLTAR")
            print("--------------------------")
            opcao = self.le_inteiro("Escolha uma opção: ", lista_opcoes)
            if opcao == 0:
                return None
            else:
                return produto_por_posicao.get(opcao)

    def tela_adicionado_ao_carrinho(self):
        print("----------------------------")
        print("ADICIONADO COM SUCESSO")
        print("0 - OK")
        print("----------------------------")
        opcao = self.le_inteiro("Escolha uma opção: ", [0])
        return opcao

    def tela_ver_carrinho(self, carrinho):
        print("----------------------------")
        if len(carrinho) == 0:
            print("CARRINHO VAZIO")
        for item in carrinho:
            print("- {}".format(item.nome))
        print("0 - VOLTAR")
        print("----------------------------------------")
        opcao = self.le_inteiro("Escolha uma opcao: ", [0])
        return opcao

    def lista (self, tamanho):
        nova_lista = []
        for i in range (tamanho + 1):
            nova_lista.append(i)
        return nova_lista

    def remove_do_carrinho (self, carrinho):
        print("----------------------------")
        tamanho_da_lista = self.lista(len(carrinho))

        opcao = self.le_inteiro("Escolha um numero para remover o produto ao carrinho: ", tamanho_da_lista)
        if opcao == 0:
            print("----------------------------")
            return None
        else:
            print("REMOVIDO COM SUCESSO")
            print("----------------------------")
            return opcao

    def limpar_carrinho (self):
        print("1 - LIMPAR")
        print("0 - VOLTAR")
        print("----------------------------------------")
        opcao = self.le_inteiro("Escolha uma opcao: ", [1, 0])
        if opcao == 1:
            return True
        else:
            return False

    def comprar (self, valor):
        print("Deu {} reais a compra".format(valor))
        print("1 - PAGAR")
        print("0 - VOLTAR")
        print("----------------------------------------")
        opcao = self.le_inteiro("Escolha uma opcao: ", [1, 0])
        if opcao == 1:
            return True
        else:
            return False

    def pagamento (self, desconto):
        if desconto == 0:
            input("Coloque o endereço de sua carteira: ")
            print("Transação concluida com sucesso")
            print("---------------------------------")
        else:
            print("Alguns itens foram removidos do carrinho por falta de estoque, logo, Você teve uma correção de -{} reais no preço".format(desconto))
            input("Coloque o endereço de sua carteira: ")
            print("Transação concluida com sucesso")
            print("---------------------------------")