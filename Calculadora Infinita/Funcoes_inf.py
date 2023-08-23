from time import sleep
import sys


def descrever():
    print('='*40+' CALCULADORA INFINITA '+'='*40)
    print('Instruções:')
    print('1 => Digite Quatro Números:')
    print('2 => Será calculado a soma, subtração, multiplicação e divisão entre eles')
    print('3 => Resultados em decimais serão convertidos para Inteiros')
    print('4 => Os 4 Resultados serão usados para calcular novamente sua soma, subtração, multiplicação e divisão')
    print('5 => Números acima de 99 voltam para a unidade 01 no final')
    print('6 => O Processo se repete a cada 5 segundos')
    input('Pressione ENTER para continuar...')


def verifica(x1,x2,x3,x4):
    if x1==0 or x1>99:
        x1 = 1
    if x2==0 or x2>99:
        x2 = 1
    if x3==0 or x3>99:
        x3 = 1
    if x4==0 or x4>99:
        x4 = 1


def atribuicao(soma,sub,mult,div,x1,x2,x3,x4):
    x1=soma
    x2=sub
    x3=mult
    x4=div

    verifica(x1,x2,x3,x4)
    if x1==1 and x2==1 and x3==1 and x4==1:
        pass
    else:
        repeticao(x1,x2,x3,x4)
 

def repeticao(x1,x2,x3,x4):
    print('-'*40)
    soma = int(x1+x2+x3+x4)
    sub = int(x1-x2-x3-x4)
    mult = int(x1*x2*x3*x4)

    if x1==0 or x2==0 or x3==0 or x4==0:
        div = 1
    else:
        div = int(x1/x2/x3/x4)
    
    print(f'{x1} + {x2} + {x3} + {x4} = {soma}')
    print(f'{x1} - {x2} - {x3} - {x4} = {sub}')
    print(f'{x1} * {x2} * {x3} * {x4} = {mult}')
    print(f'{x1} / {x2} / {x3} / {x4} = {div}')
    sleep(4)

    verifica(x1,x2,x3,x4)
    atribuicao(soma,sub,mult,div,x1,x2,x3,x4)