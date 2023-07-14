import Texto as d
import Validacoes as v
import sys
from time import sleep


def iniciar():
    d.descreve_clima()
    clima_conv = str(input('Digite a opção de conversão correspondente: '))
    clima = clima_conv.upper()
    conv_clima(clima)
    
def conv_clima(clima:str) -> float:
    while len(clima) == 0:
        print('')
        clima_conv = str(input('Digite a opção de conversão correspondente: '))
        clima = clima_conv.upper()
        conv_clima(clima)

    if clima == 'A':
        x=input('Digite o valor em ºC: ')
        v.valida_2(x,clima)
        calc=(float(x)*1.8)+32
    elif clima == 'B':
        x=input('Digite o valor em ºC: ')
        v.valida_2(x,clima)
        calc=float(x)+273
    elif clima == 'C':
        x=input('Digite o valor em ºF: ')
        v.valida_2(x,clima)
        calc=((float(x)-32)*5)/9
    elif clima == 'D':
        x=input('Digite o valor em ºF: ')
        v.valida_2(x,clima)
        calc=(((float(x)-32)*5)/9)+273
    elif clima == 'E':
        x=input('Digite o valor em K: ')
        v.valida_2(x,clima)
        calc=float(x)-273
    elif clima == 'F':
        x=input('Digite o valor em K: ')
        v.valida_2(x,clima)
        calc=((float(x)-273)*1.8)+32
    
    else:
        print('OPÇÃO INVÁLIDA!')
        clima_conv = str(input('Digite a opção de conversão correspondente: '))
        clima = clima_conv.upper()
        conv_clima(clima)

    finaliza_clima(clima,x,calc)

def finaliza_clima(clima:str, x:float, calc:float) -> float:
    if clima == 'A':
        print(f'{x} ºC equivale a {calc} ºF')
    elif clima == 'B':
        print(f'{x} ºC equivale a {calc} K')
    elif clima == 'C':
        print(f'{x} ºF equivale a {calc} ºC')
    elif clima == 'D':
        print(f'{x} ºF equivale a {calc} K')
    elif clima == 'E':
        print(f'{x} K equivale a {calc} ºC')
    elif clima == 'F':
        print(f'{x} K equivale a {calc} ºF')
