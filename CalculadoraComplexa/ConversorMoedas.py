import Texto as d
import Validacoes as v
import sys
from time import sleep

def iniciar():
    d.descreve_moedas()
    moeda_conv = str(input('Digite a opção de conversão correspondente: '))
    moeda = moeda_conv.upper()
    conv_moeda(moeda)

def conv_moeda(moeda:str) -> float:
    while len(moeda) == 0:
        print('')
        moeda_conv = str(input('Digite a opção de conversão correspondente: '))
        moeda = moeda_conv.upper()
        conv_moeda(moeda)
    
    if moeda == 'A':
        x = input('Digite o valor em Reais: ')
        v.valida_1(x,moeda)
        calc = float(x)*0.2
    elif moeda == 'B':
        x = input('Digite o valor em Reais: ')
        v.valida_1(x,moeda)
        calc = float(x)*0.187
    elif moeda == 'C':
        x = input('Digite o valor em Reais: ')
        v.valida_1(x,moeda)
        calc = float(x)*0.16
    elif moeda == 'D':
        x = input('Digite o valor em Reais: ')
        v.valida_1(x,moeda)
        calc = float(x)*50
    elif moeda == 'E':
        x = input('Digite o valor em Reais: ')
        v.valida_1(x,moeda)
        calc = float(x)*28.57
    elif moeda == 'F':
        x = input('Digite o valor em Reais: ')
        v.valida_1(x,moeda)
        calc = float(x)*573128
    elif moeda == 'G':
        x = input('Digite o valor em Dólares: ')
        v.valida_1(x,moeda)
        calc = float(x)*5
    elif moeda == 'H':
        x = input('Digite o valor em Euros: ')
        v.valida_1(x,moeda)
        calc = float(x)*5.33
    elif moeda == 'I':
        x = input('Digite o valor em Libras: ')
        v.valida_1(x,moeda)
        calc = float(x)*6.22
    elif moeda == 'J':
        x = input('Digite o valor em Pesos Argentinos: ')
        v.valida_1(x,moeda)
        calc = float(x)*0.02
    elif moeda == 'K':
        x = input('Digite o valor em Ienes: ')
        v.valida_1(x,moeda)
        calc = float(x)*0.035
    elif moeda == 'L':
        x = input('Digite o valor em Bol Venezuelanos: ')
        v.valida_1(x,moeda)
        calc = float(x)*0.0000017

    else:
        print('OPÇÃO INVÁLIDA!')
        moeda_conv = str(input('Digite a opção de conversão correspondente: '))
        moeda = moeda_conv.upper()
        conv_moeda(moeda)

    finaliza_moeda(moeda,x,calc)

def finaliza_moeda(moeda:str, x:float, calc:float) -> float:
    if moeda == 'A':
        print(f'R$ {x} equivale a {calc} Dólares')
    elif moeda == 'B':
        print(f'R$ {x} equivale a {calc} Euros')
    elif moeda == 'C':
        print(f'R$ {x} equivale a {calc} Libras')
    elif moeda == 'D':
        print(f'R$ {x} equivale a {calc} Pesos Argentinos')
    elif moeda == 'E':
        print(f'R$ {x} equivale a {calc} Ienes')
    elif moeda == 'F':
        print(f'R$ {x} equivale a {calc} Bol Venezuelanos')
    elif moeda == 'G':
        print(f'{x} Dólares equivale a R$ {calc}')
    elif moeda == 'H':
        print(f'{x} Euros equivale a R$ {calc}')
    elif moeda == 'I':
        print(f'{x} Libras equivale a R$ {calc}')
    elif moeda == 'J':
        print(f'{x} Pesos Argentinos equivale a R$ {calc}')
    elif moeda == 'K':
        print(f'{x} Ienes equivale a R$ {calc}')
    elif moeda == 'L':
        print(f'{x} Bol Venezuelanos equivale a R$ {calc}')
