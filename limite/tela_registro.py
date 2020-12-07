from limite.tela_base import TelaBase
import PySimpleGUI as sg


class TelaRegistro(TelaBase):

    def __init__(self, controlador):
        self.__controlador = controlador

    def mostra_opcoes(self):
        return self.lista_opcoes(
            ['Ver produtos incluidos', 'Ver produtos excluidos', 'Ver produtos alterados',
                'Ver produto mais caro', 'Ver produto mais barato', 'Ver clientes cadastrados'], 'Registros'
        )

    def tela_ver_incluidos(self, produtos_incluidos):
        return self.lista_produtos(produtos_incluidos, 'Produtos incluidos')

    def tela_ver_excluidos(self, produtos_excluidos):
        return self.lista_produtos(produtos_excluidos, 'Produtos excluidos')

    def tela_ver_alterados(self, produtos_alterados):
        return self.lista_produtos(produtos_alterados, 'Produtos alterados')

    def tela_ver_mais_caro(self, produto_mais_caro):
        return self.lista_produtos([produto_mais_caro], 'Produto mais caro')

    def tela_ver_mais_barato(self, produto_mais_barato):
        return self.lista_produtos([produto_mais_barato], 'Produto mais barato')

    def tela_ver_clientes_incluidos(self, lista_clientes):
        return self.lista_clientes(lista_clientes, 'Clientes adicionados')
