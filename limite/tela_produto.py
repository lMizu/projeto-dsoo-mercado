from limite.tela_base import TelaBase
import PySimpleGUI as sg


class TelaProduto(TelaBase):

    def __init__(self, controlador):
        self.__controlador = controlador

    def check_values(self, values):
        try:
            if len(values[0]) == 0 or len(values[1]) == 0 or len(values[2]) == 0:
                raise ValueError
            price_to_float = float('{:2f}'.format(float(values[1])))
            stock_to_int = int(values[2])

            return [values[0], price_to_float, stock_to_int]
        except:
            self.dialogBox('Erro', 'Algum campo contém erro!', True)

    def mostra_opcoes(self):
        return self.lista_opcoes(
            ['Ver produtos', 'Cadastrar produtos'], 'Modificar produtos'
        )

    def tela_ver_produtos(self, produtos):
        sg.ChangeLookAndFeel('Reddit')

        switcher = {}
        if len(produtos) == 0:
            layout = [
                [sg.Text('Não há produtos cadastrados', size=(30, 1))],
            ]
        else:
            layout = []
            for i in range(len(produtos)):
                layout.append(
                    [sg.Button(produtos[i].nome, size=(20, 2))]
                )
                switcher[produtos[i].nome] = produtos[i]
        layout.append(
            [sg.Button('   Voltar   ', size=(20, 1))]
        )

        window = sg.Window('Produtos').Layout(layout)
        button = window.Read()

        switcher['   Voltar   '] = 0

        window.close()
        return switcher.get(button[0])

    def tela_cadastra_produto(self):
        while True:
            sg.ChangeLookAndFeel('Reddit')

            layout = [
                [sg.Text('Nome', size=(20, 1)),
                sg.InputText('', size=(20, 2))],
                [sg.Text('Preço', size=(20, 1)),
                sg.InputText(float(), size=(20, 2))],
                [sg.Text('Estoque', size=(20, 1)),
                sg.InputText(int(), size=(20, 2))],
                [sg.Button('   Voltar   ', size=(10, 1)),sg.Button('Cadastrar', size=(10, 1))]
            ]

            window = sg.Window('Cadastrar produtos').Layout(layout)
            button, value = window.Read()

            if button == 'Cadastrar':
                values = [value[0], value[1], value[2]]
                checked_values = self.check_values(values)
                if checked_values != None:
                    window.close()
                    return checked_values
            else:
                window.close()
                return None

            window.close()

    def tela_edita_produto(self, produto):
        sg.ChangeLookAndFeel('Reddit')

        layout = [
            [sg.Text('Nome', size=(20, 1)),
             sg.InputText(produto.nome, size=(20, 2))],
            [sg.Text('Preço', size=(20, 1)),
             sg.InputText(produto.preco, size=(20, 2))],
            [sg.Text('Estoque inicial', size=(20, 1)),
             sg.InputText(produto.estoque, size=(20, 2))],
            [sg.Button('  Voltar  '), sg.Submit('Atualizar'), sg.Submit('Deletar')]
        ]

        window = sg.Window('Cadastro de produto').Layout(layout)
        button, value = window.Read()

        if button == '  Voltar  ':
            return 0
        elif button == 'Deletar':
            return 1
        elif button == 'Atualizar':
            formated_values = self.check_values([value[0], value[1], value[2]])
            if (formated_values != 'Error'):
                return formated_values
            else:
                # mostrar erro nos campos
                return ""
