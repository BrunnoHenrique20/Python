import Funcoes_inf as f
from time import sleep
import sys

# Iniciar a calculadora com X1 e X2 valores aleatórios
# usar apenas SOMA e SUBTRAÇÃO com o resultados dos resultados

f.descrever()
print('')
x1 = int(input('Digite o primeiro número: '))
x2 = int(input('Digite o segundo número: '))
x3 = int(input('Digite o terceiro número: '))
x4 = int(input('Digite o quarto número: '))

f.repeticao(x1,x2,x3,x4)

infinite = True
while infinite == True:
    f.repeticao(x1,x2,x3,x4)
    infinite=False

print('')
print('EXECUÇÃO TERMINADA!')


    

    # x1 = x1+x2+x3+x4
    # x2 = x1-x2-x3-x4
    # x3 = x1*x2*x3*x4
    # x4 = int(x1/x2/x3/x4)
