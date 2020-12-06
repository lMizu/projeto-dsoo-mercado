from limite.tela_le_inteiro import TelaLeInteiro
import PySimpleGUI as sg

class TelaCliente(TelaLeInteiro):
    def __init__ (self, controlador):
        self.__controlador = controlador

    def mostra_tela_opcoes (self):
        sg.ChangeLookAndFeel('Reddit')

        layout = [
                    [sg.Button('Login', size=(20, 2))],
                    [sg.Button('Cadastro', size=(20, 2))],
                    [sg.Button('Voltar', size=(20, 2))]
                ]
        window = sg.Window('Cliente').Layout(layout)
        button = window.Read()

        if button[0] == 'Login':
            opcao = 1
        if button[0] == 'Cadastro':
            opcao = 2
        if button[0] == 'Voltar': 
            opcao = 0
        window.close()
        return opcao

    def tela_login_cliente (self):
        sg.ChangeLookAndFeel('Reddit')

        layout = [
                    [sg.Text('Coloque seu nome ou CPF', size=(20, 1)), sg.InputText('', size=(10, 2))],
                    [sg.Text('Coloque sua senha', size=(20, 1)), sg.InputText('', size=(10, 2))],
                    [sg.Submit('Logar'), sg.Button('Voltar')]
                ]
        window = sg.Window('Cliente').Layout(layout)
        button, value = window.Read()

        window.close()
        if button == 'Logar':
            return  [value[0], value[1]]
        else:
            return None
        
    def cadastro_sucesso (self):
        sg.ChangeLookAndFeel('Reddit')

        layout = [
                    [sg.Text('Cadastrado com sucesso!')],
                    [sg.Button('Voltar')]
                ]
        
        window = sg.Window('Cliente').Layout(layout)
        window.Read()
        window.close()
    
    def fracasso_nome (self):
        sg.ChangeLookAndFeel('Reddit')

        layout = [
                    [sg.Text('Este nome ja foi escolhido')],
                    [sg.Button('Tentar novamente')]
                ]
        
        window = sg.Window('Cliente').Layout(layout)
        window.Read()
        window.close()
    
    def fracasso_cpf (self):
        sg.ChangeLookAndFeel('Reddit')

        layout = [
                    [sg.Text('Este CPF ja foi escolhido')],
                    [sg.Button('Tentar novamente')]
                ]
        
        window = sg.Window('Cliente').Layout(layout)
        window.Read()
        window.close()

    def tela_erro(self):
        sg.ChangeLookAndFeel('Reddit')

        layout = [
                    [sg.Text('Dados incorretos')],
                    [sg.Button('Tentar novamente')]
                ]
        
        window = sg.Window('Cliente').Layout(layout)
        window.Read()
        window.close()
        
    def tela_cliente (self, nome):
        sg.ChangeLookAndFeel('Reddit')

        layout = [
                    [sg.Button('Ver produtos', size=(20, 2))],
                    [sg.Button('Ver carrinho', size=(20, 2))],
                    [sg.Button('Remover produto do carrinho', size=(20, 2))],
                    [sg.Button('Limpar carrinho', size=(20, 2))],
                    [sg.Button('Finalizar compra', size=(20, 2))],
                    [sg.Button('Sair', size=(20, 2))]
                ]
        window = sg.Window('Cliente').Layout(layout)
        button = window.Read()

        if button[0] == 'Ver produtos':
            opcao = 1
        if button[0] == 'Ver carrinho':
            opcao = 2
        if button[0] == 'Remover produto do carrinho': 
            opcao = 3
        if button[0] == 'Limpar carrinho':
            opcao = 4
        if button[0] == 'Finalizar compra':
            opcao = 5
        if button[0] == 'Sair': 
            opcao = 0
        window.close()

        return opcao

    def tela_cadastro (self):
        while True:
            sg.ChangeLookAndFeel('Reddit')

            layout = [
                        [sg.Text('Coloque seu nome:', size=(20, 1)), sg.InputText('', size=(10, 2))],
                        [sg.Text('Coloque seu CPF:', size=(20, 1)), sg.InputText('', size=(10, 2))],
                        [sg.Text('Coloque sua senha:', size=(20, 1)), sg.InputText('', size=(10, 2))],
                        [sg.Text('Coloque sua senha novamente:', size=(20, 1)), sg.InputText('', size=(10, 2))],
                        [sg.Button('Cadastrar'), sg.Button('Voltar')]
                    ]
            
            window = sg.Window('Cadastro').Layout(layout)
            button, value = window.Read()
            senha = self.senha_igual(value[2], value[3])
            if senha != None:
                if button == 'Cadastrar':
                    window.close()
                    return  [value[0], value[1], senha]
                else:
                    window.close()
                    return None
            window.close()
        
    def senha_igual (self, senha1, senha2):
        try:
            if senha1 != senha2:
                raise ValueError
            return senha1
        except ValueError:
            sg.ChangeLookAndFeel('Reddit')

            layout = [
                        [sg.Text('Valores discrepantes, coloque senhas iguais')],
                        [sg.Button('Tentar novamente')]
                    ]
            
            window = sg.Window('Cliente').Layout(layout)
            window.Read()
            window.close()

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
        sg.ChangeLookAndFeel('Reddit')

        layout = [
                    [sg.Button('Limpar', size=(20, 2))],
                    [sg.Button('Voltar', size=(20, 2))]
                ]
        window = sg.Window('Cliente').Layout(layout)
        button = window.Read()

        if button[0] == 'Limpar':
            opcao = True
        else:
            opcao = False

        window.close()
        return opcao

    def limpar_sucesso (self):
        sg.ChangeLookAndFeel('Reddit')

        layout = [
                    [sg.Text('Carrinho Limpo!')],
                    [sg.Button('Voltar')]
                ]
        
        window = sg.Window('Cliente').Layout(layout)
        window.Read()
        window.close()

    def comprar (self, valor):
        sg.ChangeLookAndFeel('Reddit')

        layout = [
                    [sg.Text("Deu {} reais a compra".format(valor))],
                    [sg.Button('Ir para o pagamento', size=(20, 2))],
                    [sg.Button('Voltar', size=(20, 2))]
                ]
        window = sg.Window('Cliente').Layout(layout)
        button = window.Read()

        if button[0] == 'Ir para o pagamento':
            opcao = True
        else:
            opcao = False

        window.close()
        return opcao

    def pagamento (self, desconto):
        sg.ChangeLookAndFeel('Reddit')

        layout = [
                    [sg.Input("Coloque o endereço de sua carteira")],
                    [sg.Button('Pagar', size=(20, 2))]
                ]
        window = sg.Window('Cliente').Layout(layout)
        window.Read()

        if desconto == 0:
            self.pagamento_sucesso()
        else:
            self.pagamento_desconto(desconto)

        window.close()

    def pagamento_sucesso (self):
        sg.ChangeLookAndFeel('Reddit')

        layout = [
                    [sg.Text("Transação concluida com sucesso")],
                    [sg.Button('Voltar', size=(20, 2))]
                ]
        window = sg.Window('Cliente').Layout(layout)
        window.Read()
        window.close()

    def pagamento_desconto (self, desconto):
        sg.ChangeLookAndFeel('Reddit')

        layout = [  
                    [sg.Text("Alguns itens foram removidos do carrinho por falta de estoque, logo, Você teve uma correção de -{} reais no preço".format(desconto))],
                    [sg.Text("Transação concluida com sucesso")],
                    [sg.Button('Voltar', size=(20, 2))]
                ]
        window = sg.Window('Cliente').Layout(layout)
        window.Read()
        window.close()
