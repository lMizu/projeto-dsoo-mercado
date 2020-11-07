from limite.tela_le_inteiro import TelaLeInteiro


class TelaInicial(TelaLeInteiro):
    def __init__ (self, controlador):
        self.__controlador = controlador

    def mostra_tela_opcoes (self):
        print("-----------------------------")
        print("ESCOLHA ENTRE 1 2 E 0 PARA NAVEGAR")
        print("1 - Entrar como CLIENTE")
        print("2 - Entrar como ADMINISTRADOR")
        print("0 - FECHAR PROGRAMA")
        print("-----------------------------")
        opcao = self.le_inteiro("Escolha uma opcao: ", [1, 2, 0])
        return opcao
