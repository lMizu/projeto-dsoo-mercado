

class TelaCliente:
    def __init__ (self, controlador):
        self.__controlador = controlador

    def le_inteiro (self, mensagem: str = "", inteiros_validos: [] = None):
        while True:
            valor_lido = input(mensagem)
            try:
                inteiro = int(valor_lido)
                if inteiros_validos and inteiro not in inteiros_validos:
                    raise ValueError
                return inteiro
            except ValueError:
                print("Valor incorreto, coloque um um destes valores {}".format(inteiros_validos))


    def mostra_tela_opcoes (self):
        print("--------------------------")
        print("ESCOLHA 1 2 3 PARA NAVEGAR")
        print("1 - LOGAR")
        print("2 - CADASTRAR")
        print("3 - VOLTAR")
        opcao = self.le_inteiro("Escolha uma opcao: ", [1, 2, 3])
        return opcao

    def tela_cliente(self):
        pass

    def tela_cadastro (self):
        return [1, 2, 3]
