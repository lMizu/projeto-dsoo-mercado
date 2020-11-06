from limite.tela_le_inteiro import TelaLeInteiro

class TelaProduto(TelaLeInteiro):
    
    def __init__(self, controlador):
        self.__controlador = controlador

    def define_nome(self):
        while True:
            entrada_nome = input(str("Nome do produto: "))
            if len(entrada_nome) > 0:
                return entrada_nome
            else:
                print("Adicione um nome ao produto")       

    def define_preco(self):
        while True:
            entrada_preco = input("Preço do produto: ")
            try:
                novo_preco = float(entrada_preco)
                preco = float("{:.2f}".format(novo_preco))
                return preco
            except:
                print("Valor inválido, coloque um número nestes modelos: 21.124, 5, 2.0")

    def define_estoque(self):
        while True:
            entrada_estoque = input("Quantidade do estoque: ")
            try:
                estoque = int(entrada_estoque)
                return estoque
            except:
                print("Valor inválido, coloque um número inteiro")

    def mostra_opcoes(self):
        print("--------------------------")
        print("ESCOLHA 1 2 3 OU 0 PARA NAVEGAR")
        print("1 - VER PRODUTOS")
        print("2 - CADASTRAR PRODUTO")
        print("3 - ALTERAR PRODUTO")
        print("4 - DELETAR PRODUTO")
        print("0 - VOLTAR")
        print("--------------------------")
        opcao = self.le_inteiro("Escolha uma opção: ", [1, 2, 3, 4, 0])
        return opcao

    def tela_ver_produto(self, produtos):
        print("--------------------------")
        print("PRODUTOS CADASTRADOS:")
        if len(produtos) == 0:
            print("Não há produtos cadastrados")
        i = 1
        for produto in produtos:
            print("{} - {} / R${} / x{}".format(i, produto.nome, produto.preco, produto.estoque))
            i += 1
        return print("0 - VOLTAR")

    def tela_cadastra_produto(self):
        print("--------------------------")
        print("CADASTRO DE PRODUTO")
        nome = self.define_nome()
        preco = self.define_preco()
        estoque = self.define_estoque()
        print("--------------------------")
        print("1 - CONFIRMAR")
        print("0 - VOLTAR")
        print("--------------------------")
        opcao = self.le_inteiro("Escolha uma opção: ", [1, 0])
        if opcao == 1:
            return [nome, preco, estoque]
        elif opcao == 0:
            return None

    def tela_altera_produto(self, produtos):
        print("--------------------------")
        if len(produtos) == 0:
            print("Não há produtos cadastrados")
        else:
            print("ESCOLHA O PRODUTO QUE DESEJA ALTERAR")
        posicao = 0
        produto_por_posicao = {}
        lista_opcoes = []
        for produto in produtos:
            posicao += 1
            print("{} - {} / R${} / x{}".format(posicao, produto.nome, produto.preco, produto.estoque))
            produto_por_posicao[posicao] = produto
            lista_opcoes.append(posicao)
        lista_opcoes.append(0)
        print("0 - VOLTAR")
        print("--------------------------")
        opcao = self.le_inteiro("Escolha uma opção: ", lista_opcoes)
        if opcao == 0:
            return None
        else:
            produto_alterado = produto_por_posicao.get(opcao)
            novo_nome = self.define_nome()
            novo_preco = self.define_preco()
            novo_estoque = self.define_estoque()
            return [produto_alterado, novo_nome, novo_preco, novo_estoque]

    def tela_deleta_produto(self, produtos):
        print("--------------------------")
        if len(produtos) == 0:
            print("Não há produtos cadastrados")
        else:
            print("ESCOLHA O PRODUTO QUE DESEJA DELETAR")
        posicao = 0
        produto_por_posicao = {}
        lista_opcoes = []
        for produto in produtos:
            posicao += 1
            print("{} - {}".format(posicao, produto.nome))
            produto_por_posicao[posicao] = produto
            lista_opcoes.append(posicao)
        lista_opcoes.append(0)
        print("0 - VOLTAR")
        print("--------------------------")
        opcao = self.le_inteiro("Escolha uma opção: ", lista_opcoes)
        if opcao == 0:
            return None
        else:
            produto_alterado = produto_por_posicao.get(opcao)
            while True:
                resposta = input(str("Tem certeza que quer deletar o produto {}? s/n".format(produto_alterado.nome)))
                if resposta == "s":
                    return [produto_alterado]
                elif resposta == "n":
                    return None
                else:
                    print("Resposta inválida, por favor responda com s ou n")
            
            


    
    
