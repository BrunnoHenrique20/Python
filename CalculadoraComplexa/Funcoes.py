#EM CONSTRUÇÃO
import Texto as d
import Validacoes as v
import Inicio as i
import ConversorMoedas, ConversorTemperatura, ConversorTempo, ConversorMedidas
import sys
from math import factorial
from math import fmod
from math import hypot
from math import log
from math import nextafter
from math import pow
from math import sqrt
from operator import neg
from time import sleep

'''O módulo Upper converte o que foi digitado na operação em Letra Maiúscula (deixando o resultado
    de ser Case sensitive)'''

def digitar():
    n1,n2='N','N'
    verificar1, verificar2 = False,False
    while verificar1==False:
        n1 = input('Digite o primeiro número: ')
        verificar1 = v.is_number(n1)
    while verificar2==False:
        n2 = input('Digite o segundo número: ')
        verificar2 = v.is_number(n2)
    return float(n1),float(n2)

def digitar_2():
    n1,n2,n3='N','N','N'
    verificar1, verificar2, verificar3 = False,False,False
    while verificar1==False:
        n1 = input('Digite o primeiro número: ')
        verificar1 = v.is_number(n1)
    while verificar2==False:
        n2 = input('Digite o segundo número: ')
        verificar2 = v.is_number(n2)
    while verificar3==False:
        n3 = input('Digite o terceiro número: ')
        verificar3 = v.is_number(n3)
    return float(n1),float(n2),float(n3)

def calculadora(operacao: str, pagina:int):
    if operacao == 'A':
        n1,n2 = digitar()
        print('-'*40)
        soma(n1,n2)
    elif operacao == 'B':
        n1,n2 = digitar()
        print('-'*40)
        sub(n1,n2)
    elif operacao == 'C':
        n1,n2 = digitar()
        print('-'*40)
        mult(n1,n2)

    elif operacao == 'D':
        n1,n2 = digitar()
        print('-'*40)
        if n1==0 or n2==0:
            print('ERRO: Não é possivel dividir nenhum número por 0 ou ter um número divisivel por 0!')
            print('[---O programa será finalizado---]')
            sys.exit()
        else:
            div(n1,n2)

    elif operacao=='E':
        n1 = float(input('Digite um número: '))
        print('-'*40)
        quadrado(n1)

    elif operacao =='F':
        n1,n2 = digitar()
        pot(n1,n2)

    elif operacao=='G':
        n1 = float(input('Digite um número: '))
        print('-'*40)
        raiz(n1)

    elif operacao == 'H':
        n1,n2 = digitar()
        porcent(n1,n2)

    elif operacao=='I':
        n1 = int(input('Digite um número: '))
        print('-'*40)
        fatorial(n1)

    elif operacao=='J':
        n1 = int(input('Digite um número: '))
        print('-'*40)
        logt(n1)

    elif operacao=='K':
        n1,n2,n3 = digitar_2()
        print('-'*40)
        segundograu(n1,n2,n3)

    elif operacao=='L':
        x=str(input('Quantos números deseja digitar? '))
        quant=v.valida_quant(x)
        resultado=calc_media(quant)
        conv_result = float("{:.2f}".format(resultado))
        print(f'A média dos números digitados é {conv_result}')

    elif operacao=='M':
        ConversorMoedas.iniciar()

    elif operacao=='N':
        ConversorTemperatura.iniciar()

    elif operacao=='O':
        ConversorTempo.iniciar(pagina)

    elif operacao=='P':
        ConversorMedidas.iniciar(pagina)

    else:
        operacao_conv = str(input('Digite a operação desejada: '))
        operacao = operacao_conv.upper()
        calculadora(operacao,pagina)

    loop(operacao)

def soma(n1: float, n2: float) -> float:
    soma = n1 + n2
    return print(f'Soma: {soma}')

def sub(n1: float, n2: float) -> float:
    sub = n1 - n2
    return print(f'Subtração: {sub}')

def mult(n1: float, n2: float) -> float:
    mult = n1 * n2
    return print(f'Multiplicação: {mult}')

def div(n1: float, n2: float) -> float:
    div=float("{:.2f}".format(n1/n2))
    return print(f'Divisão: {div}')

def quadrado(n1: float) -> float:
    quadrado = n1 * n1
    return print(f'{n1} elevado ao quadrado é igual a {quadrado}')

def pot(n1: float, n2: float) -> float:
#    pot = (n1)**n2
#    return print(f'Potenciação: {pot}')
    pot = pow(n1,n2)
    return print(f'Potenciação: {pot}')

'''O Módulo pow é Exclusivo para fazer a potenciação automaticamente sem a necessidade de inserir um código
    Deixei comentado acima para ver como ficaria sem a importação de pow'''

def raiz(n1: float) -> float:
    raiz = float("{:.2f}".format(sqrt(n1)))
    return print(f'A raiz quadrada de {n1} é {raiz}')

def porcent(n1: float, n2: float) -> float:
    n2_conv = n2 / 100
    result = float("{:.2f}".format(n1*n2_conv))
    return print(f'{n2}% de {n1} é igual a {result}')

def fatorial(n1: int) -> int:
    '''O Resultado em Fatorial também é convertido para Inteiro, pois não aceita float'''
    
    fator = factorial(n1)
    return print(f'O Fatorial de {n1} é igual a {fator}')

def logt(n1: float) -> float:
    logt = float("{:.4f}".format(log(n1,10)))
    return print(f'O Logarítmo de {n1} é {logt}')

'''O Calculo do Logaritmo tem como base padrão a base 10'''

def segundograu(n1: float, n2: float, n3: float) -> float:
    delta = neg((n2**n2)-4*n1*n3)
    baskara_pos = (-n2 + sqrt(neg(float(delta))) / 2*n1)
    baskara_neg = (-n2 - sqrt(neg(float(delta))) / 2*n1)
    conv_delta = float("{:.2f}".format(delta))
    conv_baskara_pos = float("{:.2f}".format(baskara_pos))
    conv_baskara_neg = float("{:.2f}".format(baskara_neg))

    print(f'Equação: {n1}x² + {n2}x + {n3}')
    print(f'Valor de Delta: {conv_delta}')
    print(f'Desvio de Baskara Positivo: {conv_baskara_pos}')
    print(f'Desvio de Baskara Negativo: {conv_baskara_neg}')

'''Foi utilizado o módulo NEG ele converte numeros negativos (-5) em positivos (5) prevenindo que
o valor de Delta fique negativo'''

def calc_media(quant):
    i=0
    while i < quant:
        if i==0:
            soma_media=float(0)

        x=input(f'Digite o {i+1}º valor: ')
        z=v.contem_float(x)

        if z==True:
            soma_media = soma_media + float(x)
            i=i+1
        else:
            print('Letras e Números Negativos não são aceitos, digite novamente!')
            sleep(2)
    
    resultado=soma_media/quant
    resultado=float("{:.2f}".format(resultado))
    return resultado

def loop(operacao:str):
    print('')
    print('ENTER => Repetir um Novo Teste')
    print('M => Voltar ao Menu Principal')
    print('S => Sair do Programa')
    loop='X'
    while loop not in ['','M','S']:
        loop=str(input('Escolha uma opção: ')).upper()

    if loop=='M':
        op=i.inicial()
        calculadora(op,1)
    elif loop=='S':
        sys.exit()
    elif loop=='':
        if operacao=='A':
            calculadora('A',1)
        elif operacao=='B':
            calculadora('B',1)
        elif operacao=='C':
            calculadora('C',1)
        elif operacao=='D':
            calculadora('D',1)
        elif operacao=='E':
            calculadora('E',1)
        elif operacao=='F':
            calculadora('F',1)
        elif operacao=='G':
            calculadora('G',1)
        elif operacao=='H':
            calculadora('H',1)
        elif operacao=='I':
            calculadora('I',1)
        elif operacao=='J':
            calculadora('J',1)
        elif operacao=='K':
            calculadora('K',1)
        elif operacao=='L':
            calculadora('L',1)
        elif operacao=='M':
            calculadora('M',1)
        elif operacao=='N':
            calculadora('N',1)
        elif operacao=='O':
            calculadora('O',1)
        elif operacao=='P':
            calculadora('P',1)
