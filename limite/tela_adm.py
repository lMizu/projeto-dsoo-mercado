from limite.tela_le_inteiro import TelaLeInteiro

class TelaAdm(TelaLeInteiro):
    def __init__ (self, controlador):
        self.__controlador = controlador

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
        print("ESCOLHA ENTRE 1 2 E 0 PARA NAVEGAR")
        print("1 - MODIFICAR PRODUTOS")
        print("2 - VER REGISTROS")
        print("0 - VOLTAR")
        print("-----------------------------")
        opcao = self.le_inteiro("Escolha uma opcao: ", [1, 2, 0])
        return opcao