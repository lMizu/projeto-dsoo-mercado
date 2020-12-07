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
            for produto in produtos:
                print(produto)
                layout.append(
                    [sg.Button(produto.nome, size=(20, 2))]
                )
                switcher[produto.nome] = produto
        layout.append(
            [sg.Button('   Voltar   ', size=(20, 2))]
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
                [sg.Button('   Voltar   ', size=(10, 1)),
                 sg.Submit('Cadastrar', size=(10, 1))]
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
        while True:
            sg.ChangeLookAndFeel('Reddit')

            layout = [
                [sg.Text('Nome', size=(20, 1)),
                sg.InputText(produto.nome, size=(20, 2))],
                [sg.Text('Preço', size=(20, 1)),
                sg.InputText(produto.preco, size=(20, 2))],
                [sg.Text('Estoque inicial', size=(20, 1)),
                sg.InputText(produto.estoque, size=(20, 2))],
                [sg.Button('  Voltar  '), sg.Submit(
                    'Atualizar'), sg.Button('Deletar')]
            ]

            window = sg.Window('Editar produto').Layout(layout)
            button, value = window.Read()

            if button == '  Voltar  ':
                window.close()
                return 0
            elif button == 'Deletar':
                self.dialogBox('Produto', 'Você deletou o produto {}'.format(produto.nome), False)
                window.close()
                return 1
            elif button == 'Atualizar':
                checked_values = self.check_values([value[0], value[1], value[2]])
                if (checked_values != None):
                    if checked_values[0] != produto.nome or checked_values[1] != produto.preco or checked_values[2] != produto.estoque:
                        self.dialogBox('Produto', 'Você atualizou o produto {} com sucesso!'.format(produto.nome), False)
                        window.close()
                        return checked_values      
                    else:
                        self.dialogBox('Produto', 'Modifique algum campo para atualizar', False)
            window.close()

