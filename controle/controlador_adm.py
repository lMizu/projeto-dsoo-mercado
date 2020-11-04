from limite.tela_adm import TelaAdm
from entidade.adm import Adm

class ControladorAdm:
    def __init__ (self):
        self.__tela_adm = TelaAdm(self)

    def inicia (self):
        self.abre_tela_adm()

    def abre_tela_adm(self):
        if self.login():
            switcher = {1: self.modificar_produto, 2: self.ver_registro, 0: self.voltar}

            while True:
                opcao  = self.__tela_adm.tela_adm()
                funcao_escolhida = switcher[opcao]
                if funcao_escolhida() == "fim":
                    return None
        else:
            return None

    def login (self):
        while True:    
            inputs = self.__tela_adm.tela_login_adm()
            if inputs == None:
                return False
            else:
                valores = self.verifica_entrada(inputs[0], inputs[1])
                if valores == True:
                    return True
                else:
                    print("dados incorretos")

    def verifica_entrada (self, nome, senha):
        if (Adm().login == nome) and (Adm().senha == senha):
            return True
        return False

    def modificar_produto (self):
        pass

    def ver_registro (self):
        pass

    def voltar (self):
        return "fim"