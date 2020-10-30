import sys

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
        print("3 - SAIR")
        print("--------------------------")
        opcao = self.le_inteiro("Escolha uma opcao: ", [1, 2, 3])
        return opcao

    def tela_login_cliente (self):
        print("----------------------------------------")
        nome = input(str("coloque seu nome de usuario ou cpf: "))
        senha = input(str("coloque sua senha: "))
        print("1 - ENTRA")
        print("2 - VOLTAR")
        print("----------------------------------------")
        opcao = self.le_inteiro("Escolha uma opcao: ", [1, 2])
        if opcao == 1:
            return [nome, senha]
        else:
            return None

    def tela_cliente (self):
        print("ESCOLHA 1 2 3 PARA NAVEGAR")
        print("1 - VER CARRINHO")
        print("2 - FINALIZAR COMPRA")
        print("3 - SAIR")
        print("--------------------------")
        opcao = self.le_inteiro("Escolha uma opcao: ", [1, 2, 3])
        return opcao

    def tela_cadastro (self):
        print("----------------------------------------")
        nome = input(str("coloque seu nome de usuario: "))
        cpf = input(str("coloque seu cpf: "))
        senha = self.senha_igual()
        print("----------------------------------------")
        print("1 - CADASTRAR")
        print("2 - VOLTAR")
        print("----------------------------------------")
        opcao = self.le_inteiro("Escolha uma opcao: ", [1, 2])
        if opcao == 1:
            return [nome, cpf, senha]
        else:
            return None

    def senha_igual (self):
        while True:
            senha1 = input(str("coloque sua senha: "))
            senha2 = input(str("coloque sua senha novamente: "))
            try:
                if senha1 != senha2:
                    raise SyntaxError
                return senha1
            except SyntaxError:
                print("Valores discrepantes, coloque senhas iguais")