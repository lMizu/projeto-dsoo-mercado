

class TelaAdm:
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

    def tela_login_adm (self):
        print("----------------------------------------")
        nome = input(str("coloque o Login: "))
        senha = input(str("coloque a Senha: "))
        print("1 - ENTRA")
        print("0 - VOLTAR")
        print("----------------------------------------")
        opcao = self.le_inteiro("Escolha uma opcao: ", [1, 0])
        if opcao == 1:
            return [nome, senha]
        else:
            return None

    def tela_adm (self):
        print("-----------------------------")
        print("Bem vindo Administrador")
        print("")
        print("ESCOLHA 1 2 3 PARA NAVEGAR")
        print("1 - MODIFICAR PRODUTOS")
        print("2 - VER REGISTROS")
        print("0 - VOLTAR")
        print("-----------------------------")
        opcao = self.le_inteiro("Escolha uma opcao: ", [1, 2, 0])
        return opcao