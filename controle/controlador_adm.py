from limite.tela_adm import TelaAdm
from entidade.adm import Adm
from controle.controlador_produto import ControladorProduto
from controle.controlador_registro import ControladorRegistro


class ControladorAdm:
    def __init__ (self):
        self.__tela_adm = TelaAdm(self)
        self.__controlador_produto = ControladorProduto()
        self.__controlador_registro = ControladorRegistro()

    @property
    def controlador_produto (self):
        return self.__controlador_produto

    @property
    def controlador_registro (self):
        return self.__controlador_registro

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
    def modificar_produto (self):
        self.__controlador_produto.inicia()

    def ver_registro (self):
        self.__controlador_registro.inicia()

    def voltar (self):
        return "fim"

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
