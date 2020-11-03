import sys

class TelaProduto:
    
    def __init__(self, controlador):
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
                print("Valor incorreto, coloque um destes valores {}".format(inteiros_validos))

    def corrige_float(self, valor):
        try:
            novo_valor = float(valor)
            valor_formatado = float("{:.2f}".format(novo_valor))
            return valor_formatado
        except:
            print("Valor inválido, coloque um número nestes modelos: 21.124, 5, 2.0")


    def mostra_opcoes(self):
        print("--------------------------")
        print("ESCOLHA 1 2 3 PARA NAVEGAR")
        print("1 - VER PRODUTOS")
        print("2 - CADASTRAR PRODUTO")
        #print("3 - ALTERA PRODUTO")
        print("0 - SAIR")
        print("--------------------------")
        opcao = self.le_inteiro("Escolha uma opção: ", [1, 2, 0])
        return opcao

    def tela_ver_produto(self, produtos):
        print("--------------------------")
        for produto in produtos:
            print("- {} / R${} / x{}".format(produto.nome, produto.preco, produto.estoque))
        print("0 - VOLTAR")
        opcao = self.le_inteiro("Escolha uma opção: ", [0])
        return opcao

    def tela_cadastra_produto(self):
        print("--------------------------")
        nome = input(str("Nome do produto: "))
        preco = self.corrige_float(input("Preço do produto: "))
        estoque = int(input("Quantidade do estoque: "))
        print("--------------------------")
        print("1 - CONFIRMAR")
        print("0 - VOLTAR")
        print("--------------------------")
        opcao = self.le_inteiro("Escolha uma opção: ", [1, 0])
        if opcao == 1:
            return [nome, preco, estoque]
        elif opcao == 2:
            return None
    
