import Texto as d
from time import sleep

def inicial():
    operacao = ''
    d.descreve_menu()    # Minimizando informações
    while len(operacao) < 1:
        operacao = str(input('Digite a operação desejada: ')).upper()
        # operacao = operacao_conv.upper()

        while len(operacao) > 1:   # Comprimento do texto digitado
            print('Digite apenas a Letra correspondente!')
            sleep(2)
            print('')
            operacao = str(input('Digite a operação desejada: ')).upper()
            # operacao = operacao_conv.upper()
    return operacao