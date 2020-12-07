import PySimpleGUI as sg


class TelaBase:
    def le_inteiro(self, mensagem: str = "", inteiros_validos: [] = None):
        while True:
            valor_lido = input(mensagem)
            try:
                inteiro = int(valor_lido)
                if inteiros_validos and inteiro not in inteiros_validos:
                    raise ValueError
                return inteiro
            except ValueError:
                print("Valor incorreto, coloque um destes valores {}".format(
                    inteiros_validos))

    def lista_opcoes(self, lista_de_opcoes, titulo):
        sg.ChangeLookAndFeel('Reddit')

        layout = []
        switcher = {}

        for i in range(len(lista_de_opcoes)):
            layout.append(
                [sg.Button(lista_de_opcoes[i], size=(20, 2))]
            )
            switcher[lista_de_opcoes[i]] = i + 1
        layout.append(
                [sg.Button('  Voltar  ', size=(20, 2))]
            )
            
        window = sg.Window(titulo).Layout(layout)
        button = window.Read()

        switcher['  Voltar  '] = 0

        window.close()
        return switcher.get(button[0])

    def lista_produtos(self, produtos, titulo):
        sg.ChangeLookAndFeel('Reddit')

        if len(produtos) == 0 or produtos[0] == None:
            layout = [
                [sg.Text('Não há produtos', size=(20, 1))],
            ]
        else:
            layout = []
            for i in range(len(produtos)):
                layout.append(
                    [sg.Text('- {} / R${}'.format(produtos[i].nome,
                                                  produtos[i].preco), size=(20, 2))]
                )
        layout.append(
                [sg.Button('Voltar', size=(20, 2))]
            )

        window = sg.Window(titulo).Layout(layout)
        button = window.Read()

        switcher = {
            'Voltar': 0
        }

        window.close()
        return switcher.get(button[0])

    def lista_clientes(self, clientes, titulo):
        sg.ChangeLookAndFeel('Reddit')

        if len(clientes) == 0:
            layout = [
                [sg.Text('Não há clientes', size=(20, 1))],
            ]
        else:
            layout = []
            for i in range(len(clientes)):
                layout.append(
                    [sg.Text('Nome: {} / CPF: {}'.format(clientes[i].nome,
                                                         clientes[i].cpf), size=(20, 2))]
                )
        layout.append(
            [sg.Button('Voltar', size=(20, 2))]
        )

        window = sg.Window(titulo).Layout(layout)
        button = window.Read()

        switcher = {
            'Voltar': 0
        }

        window.close()
        return switcher.get(button[0])

    def cadastro(self, campos, titulo):
        while True:
            sg.ChangeLookAndFeel('Reddit')

            layout = []

            for i in range(len(campos)):
                layout.append(
                    [sg.Text(campos[i], size=(20, 1)),
                    sg.InputText('', size=(20, 2))]
                )
            layout.append(
                [sg.Button('   Voltar   ', size=(10, 1)),sg.Button('Cadastrar', size=(10, 1))]
            )

            window = sg.Window(titulo).Layout(layout)
            button, value = window.Read()

            window.close()
            if button == 'Cadastrar':
                values = []
                for i in range(len(campos)):
                    values.append(value[i])
                return values
            elif button == '   Voltar   ':
                return None

    def dialogBox(self, title, message, tryAgain: bool):
        sg.ChangeLookAndFeel('Reddit')

        layout = [
                    [sg.Text(message)],
                ]
        if tryAgain:
            layout.append(
                [sg.Submit('Tentar novamente')]
            )
        else:
            layout.append(
                [sg.Submit('OK')]
            )
        
        window = sg.Window(title).Layout(layout)
        window.Read()
        window.close()
