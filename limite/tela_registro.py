from limite.tela_le_inteiro import TelaLeInteiro

class TelaRegistro(TelaLeInteiro):

    def __init__(self, controlador):
        self.__controlador = controlador

    def mostra_opcoes(self):
        print("--------------------------")
        print("ESCOLHA 1 2 3 4 5 OU 0 PARA NAVEGAR")
        print("1 - VER PRODUTOS INCLUIDOS")
        print("2 - VER PRODUTOS EXCLUIDOS")
        print("3 - VER PRODUTOS ALTERADOS")
        print("4 - VER PRODUTO MAIS CARO")
        print("5 - VER PRODUTO MAIS BARATO")
        print("0 - VOLTAR")
        print("--------------------------")
        opcao = self.le_inteiro("Escolha uma opção: ", [1, 2, 3, 4, 5, 0])
        return opcao

    def tela_ver_incluidos(self, produtos_incluidos):
        print("--------------------------")
        print("PRODUTOS INCLUIDOS:")
        if len(produtos_incluidos) == 0:
            print("Não há produtos incluidos")
        for registro in produtos_incluidos:
            print("- {} / R${}".format(registro.nome_produto, registro.preco_produto))
        print("0 - VOLTAR")
        opcao = self.le_inteiro("Escolha uma opção: ", [0])
        return opcao

    def tela_ver_excluidos(self, produtos_excluidos):
        print("--------------------------")
        print("PRODUTOS EXCLUIDOS:")
        if len(produtos_excluidos) == 0:
            print("Não há produtos excluidos")
        for registro in produtos_excluidos:
            print("- {} / R${}".format(registro.nome_produto, registro.preco_produto))
        print("0 - VOLTAR")
        opcao = self.le_inteiro("Escolha uma opção: ", [0])
        return opcao

    def tela_ver_alterados(self, produtos_alterados):
        print("--------------------------")
        print("PRODUTOS ALTERADOS:")
        if len(produtos_alterados) == 0:
            print("Não há produtos alterados")
        for registro in produtos_alterados:
            print("- {} / R${}".format(registro.nome_produto, registro.preco_produto))
        print("0 - VOLTAR")
        opcao = self.le_inteiro("Escolha uma opção: ", [0])
        return opcao

    def tela_ver_mais_caro(self, produto_mais_caro):
        print("--------------------------")
        print("PRODUTO MAIS CARO:")
        print("- {}".format(produto_mais_caro))
        print("0 - VOLTAR")
        opcao = self.le_inteiro("Escolha uma opção: ", [0])
        return opcao

    def tela_ver_mais_barato(self, produto_mais_barato):
        print("--------------------------")
        print("PRODUTO MAIS BARATO:")
        print("- {}".format(produto_mais_barato))
        print("0 - VOLTAR")
        opcao = self.le_inteiro("Escolha uma opção: ", [0])
        return opcao
