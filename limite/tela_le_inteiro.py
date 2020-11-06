

class TelaLeInteiro:
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