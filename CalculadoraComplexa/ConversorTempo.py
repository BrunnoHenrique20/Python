import Texto as d
import Validacoes as v
import sys
from time import sleep

def iniciar(pagina:str):
    d.descreve_time(pagina)
    time_conv = str(input('Digite a opção correspondente: '))
    time = time_conv.upper()
    conv_time(time,pagina)

def conv_time(time:str, pagina:int):
    z=v.valida_escolha(time,pagina)
    calc_time(time,z,pagina)
    result_time(time,z,pagina)
    sys.exit()

def calc_time(time:str, x:float, pagina:int):
    if pagina==1:
        if time=='K':
            pagina=2
            d.descreve_time(pagina)
            time_conv = input('Digite a opção correspondente: ')
            time = time_conv.upper()
            conv_time(time,pagina)

        elif time=='A':
            calc=float(x)/60
            resultado=float("{:.2f}".format(calc))
        elif time=='B':
            calc=float(x)/60/60
            resultado=float("{:.2f}".format(calc))
        elif time=='C':
            calc=float(x)/60/60/24
            resultado=float("{:.2f}".format(calc))
        elif time=='D':
            calc=float(x)/60/60/24/30
            resultado=float("{:.2f}".format(calc))
        elif time=='E':
            calc=float(x)/60/60/24/30/12
            resultado=float("{:.2f}".format(calc))
        elif time=='F':
            calc=float(x)*60
            resultado=float("{:.2f}".format(calc))
        elif time=='G':
            calc=float(x)/60
            resultado=float("{:.2f}".format(calc))
        elif time=='H':
            calc=float(x)/60/24
            resultado=float("{:.2f}".format(calc))
        elif time=='I':
            calc=float(x)/60/24/30
            resultado=float("{:.2f}".format(calc))
        elif time=='J':
            calc=float(x)/60/24/30/12
            resultado=float("{:.2f}".format(calc))

    if pagina==2:
        if time=='K':
            pagina=3
            d.descreve_time(pagina)
            time_conv = str(input('Digite a opção correspondente: '))
            time = time_conv.upper()
            conv_time(time,pagina)
        elif time=='L':
            pagina=1
            d.descreve_time(pagina)
            time_conv = str(input('Digite a opção correspondente: '))
            time = time_conv.upper()
            conv_time(time,pagina)

        elif time=='A':
            calc=float(x)*60*60
            resultado=float("{:.2f}".format(calc))
        elif time=='B':
            calc=float(x)*60
            resultado=float("{:.2f}".format(calc))
        elif time=='C':
            calc=float(x)/24
            resultado=float("{:.2f}".format(calc))
        elif time=='D':
            calc=float(x)/24/30
            resultado=float("{:.2f}".format(calc))
        elif time=='E':
            calc=float(x)/24/30/12
            resultado=float("{:.2f}".format(calc))
        elif time=='F':
            calc=float(x)*24*60*60
            resultado=float("{:.2f}".format(calc))
        elif time=='G':
            calc=float(x)*24*60
            resultado=float("{:.2f}".format(calc))
        elif time=='H':
            calc=float(x)*24
            resultado=float("{:.2f}".format(calc))
        elif time=='I':
            calc=float(x)/30
            resultado=float("{:.2f}".format(calc))
        elif time=='J':
            calc=float(x)/30/12
            resultado=float("{:.2f}".format(calc))

    if pagina==3:
        if time=='K':
            pagina=2
            d.descreve_time(pagina)
            time_conv = str(input('Digite a opção correspondente: '))
            time = time_conv.upper()
            conv_time(time,pagina)

        elif time=='A':
            calc=float(x)*30*24*60*60
            resultado=float("{:.2f}".format(calc))
        elif time=='B':
            calc=float(x)*30*24*60
            resultado=float("{:.2f}".format(calc))
        elif time=='C':
            calc=float(x)*30*24
            resultado=float("{:.2f}".format(calc))
        elif time=='D':
            calc=float(x)*30
            resultado=float("{:.2f}".format(calc))
        elif time=='E':
            calc=float(x)/12
            resultado=float("{:.2f}".format(calc))
        elif time=='F':
            calc=float(x)*12*30*24*60*60
            resultado=float("{:.2f}".format(calc))
        elif time=='G':
            calc=float(x)*12*30*24*60
            resultado=float("{:.2f}".format(calc))
        elif time=='H':
            calc=float(x)*12*30*24
            resultado=float("{:.2f}".format(calc))
        elif time=='I':
            calc=float(x)*12*30
            resultado=float("{:.2f}".format(calc))
        elif time=='J':
            calc=float(x)*12
            resultado=float("{:.2f}".format(calc))

    return resultado

def result_time(time:str, x:float, pagina:int):
    resultado = calc_time(time,x,pagina)

    if pagina==1:
        if time=='A':
            print(f'{x} Segundos equivale a {resultado} Minutos')
        elif time=='B':
            print(f'{x} Segundos equivale a {resultado} Horas')
        elif time=='C':
            print(f'{x} Segundos equivale a {resultado} Dias')
        elif time=='D':
            print(f'{x} Segundos equivale a {resultado} Meses')
        elif time=='E':
            print(f'{x} Segundos equivale a {resultado} Anos')
        elif time=='F':
            print(f'{x} Minutos equivale a {resultado} Segundos')
        elif time=='G':
            print(f'{x} Minutos equivale a {resultado} Horas')
        elif time=='H':
            print(f'{x} Minutos equivale a {resultado} Dias')
        elif time=='I':
            print(f'{x} Minutos equivale a {resultado} Meses')
        elif time=='J':
            print(f'{x} Minutos equivale a {resultado} Anos')

    elif pagina==2:
        if time=='A':
            print(f'{x} Horas equivale a {resultado} Segundos')
        elif time=='B':
            print(f'{x} Horas equivale a {resultado} Minutos')
        elif time=='C':
            print(f'{x} Horas equivale a {resultado} Dias')
        elif time=='D':
            print(f'{x} Horas equivale a {resultado} Meses')
        elif time=='E':
            print(f'{x} Horas equivale a {resultado} Anos')
        elif time=='F':
            print(f'{x} Dias equivale a {resultado} Segundos')
        elif time=='G':
            print(f'{x} Dias equivale a {resultado} Minutos')
        elif time=='H':
            print(f'{x} Dias equivale a {resultado} Horas')
        elif time=='I':
            print(f'{x} Dias equivale a {resultado} Meses')
        elif time=='J':
            print(f'{x} Dias equivale a {resultado} Anos')

    elif pagina==3:
        if time=='A':
            print(f'{x} Meses equivale a {resultado} Segundos')
        elif time=='B':
            print(f'{x} Meses equivale a {resultado} Minutos')
        elif time=='C':
            print(f'{x} Meses equivale a {resultado} Horas')
        elif time=='D':
            print(f'{x} Meses equivale a {resultado} Dias')
        elif time=='E':
            print(f'{x} Meses equivale a {resultado} Anos')
        elif time=='F':
            print(f'{x} Anos equivale a {resultado} Segundos')
        elif time=='G':
            print(f'{x} Anos equivale a {resultado} Minutos')
        elif time=='H':
            print(f'{x} Anos equivale a {resultado} Horas')
        elif time=='I':
            print(f'{x} Anos equivale a {resultado} Dias')
        elif time=='J':
            print(f'{x} Anos equivale a {resultado} Meses')
