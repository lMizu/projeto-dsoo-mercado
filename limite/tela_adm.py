from limite.tela_base import TelaBase
import PySimpleGUI as sg


class TelaAdm(TelaBase):
    def __init__(self, controlador):
        self.__controlador = controlador

    def tela_login_adm(self):
        sg.ChangeLookAndFeel('Reddit')

        layout = [
            [sg.Text('Coloque seu login', size=(20, 1)),
             sg.InputText('', size=(20, 2))],
            [sg.Text('Coloque sua senha', size=(20, 1)),
             sg.InputText('', size=(20, 2))],
            [sg.Submit('Entrar'), sg.Button('Voltar')]
        ]

        window = sg.Window('Administrador').Layout(layout)
        button, value = window.Read()

        window.close()
        if button == 'Entrar':
            return [value[0], value[1]]
        else:
            return None

    def tela_adm(self):
        sg.ChangeLookAndFeel('Reddit')

        layout = [
            [sg.Button('Modificar produtos', size=(20, 2))],
            [sg.Button('Ver registros', size=(20, 2))],
            [sg.Button('Voltar', size=(20, 2))]
        ]
        window = sg.Window('Administrador').Layout(layout)
        button = window.Read()

        switcher = {
            'Modificar produtos': 1,
            'Ver registros': 2,
            'Voltar': 0
        }

        window.close()
        return switcher.get(button[0])
