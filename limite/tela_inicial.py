from limite.tela_le_inteiro import TelaLeInteiro
#from tkinter import *
import PySimpleGUI as sg

class TelaInicial(TelaLeInteiro):
    def __init__ (self, controlador):
        self.__window = None
        #self.init_components()
        self.__controlador = controlador

    def mostra_tela_opcoes (self):
        sg.ChangeLookAndFeel('Reddit')

        layout = [
                    [sg.Text('Entrar como cliente', size=(20, 1)), sg.Button('Login', size=(7, 1))],
                    [sg.Text('Entrar como administrador', size=(20, 1)), sg.Button('Gerenciar', size=(7, 1))],
                    [sg.Button('Sair', size=(29, 1))]
                ]
        window = sg.Window('Mercado').Layout(layout)
        button = window.Read()

        if button[0] == 'Login':
            opcao = 1
        if button[0] == 'Gerenciar':
            opcao = 2
        if button[0] == 'Sair': 
            opcao = 0
        window.close()
        return opcao
        
