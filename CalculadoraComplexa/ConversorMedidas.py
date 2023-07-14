import Texto as d
import Validacoes as v
import sys
from time import sleep


def iniciar(pagina:str):
    d.descreve_medidas(pagina)
    medida_conv = str(input('Digite a opção correspondente: '))
    medida = medida_conv.upper()
    conv_medidas(medida,pagina)

def conv_medidas(medida:str,pagina:str) -> str: 
    while len(medida) == 0:
        medida_conv = str(input('Digite a opção correspondente: '))
        medida = medida_conv.upper()
        conv_medidas(medida,pagina)
        while len(medida) > 1:
            medida_conv = str(input('Digite a opção correspondente: '))
            medida = medida_conv.upper()
            conv_medidas(medida,pagina)

    if pagina==1:
        if medida=='G':
            pagina=2
            d.descreve_medidas(pagina)
            medida_conv = str(input('Digite a opção correspondente: '))
            medida = medida_conv.upper()
            conv_medidas(medida,pagina)

        elif medida=='A':
            x=input('Digite o valor: ')
            v.valida_4(x,medida,pagina)

            resultado=float(x)/10
            print(f'{x} mm equivale a {resultado} CM')

        elif medida=='B':
            x=input('Digite o valor: ')
            v.valida_4(x,medida,pagina)

            resultado=(float(x)/10)/100
            print(f'{x} mm equivale a {resultado} M')

        elif medida=='C':
            x=input('Digite o valor: ')
            v.valida_4(x,medida,pagina)

            resultado=((float(x)/10)/100)/1000
            print(f'{x} mm equivale a {resultado} KM')

        elif medida=='D':
            x=input('Digite o valor: ')
            v.valida_4(x,medida,pagina)

            resultado=float(x)*10
            print(f'{x} CM equivale a {resultado} mm')

        elif medida=='E':
            x=input('Digite o valor: ')
            v.valida_4(x,medida,pagina)

            resultado=float(x)/100
            print(f'{x} CM equivale a {resultado} M')

        elif medida=='F':
            x=input('Digite o valor: ')
            v.valida_4(x,medida,pagina)

            resultado=(float(x)/100)/1000
            print(f'{x} CM equivale a {resultado} KM')

        else:
            print('OPÇÃO INVÁLIDA!')
            medida_conv = str(input('Digite a opção correspondente: '))
            medida = medida_conv.upper()
            conv_medidas(medida,pagina)

    elif pagina==2:
        if medida=='G':
            pagina=3
            d.descreve_medidas(pagina)
            medida_conv = str(input('Digite a opção correspondente: '))
            medida = medida_conv.upper()
            conv_medidas(medida,pagina)
        elif medida=='H':
            pagina=1
            d.descreve_medidas(pagina)
            medida_conv = str(input('Digite a opção correspondente: '))
            medida = medida_conv.upper()
            conv_medidas(medida,pagina)

        elif medida=='A':
            x=input('Digite o valor: ')
            v.valida_4(x,medida,pagina)

            resultado=float(x)*100
            print(f'{x} M equivale a {resultado} CM')

        elif medida=='B':
            x=input('Digite o valor: ')
            v.valida_4(x,medida,pagina)

            resultado=float(x)/1000
            print(f'{x} M equivale a {resultado} KM')

        elif medida=='C':
            x=input('Digite o valor: ')
            v.valida_4(x,medida,pagina)

            resultado=(float(x)/1000)/40000
            print(f'{x} M equivale a {resultado} Voltas ao Mundo')

        elif medida=='D':
            x=input('Digite o valor: ')
            v.valida_4(x,medida,pagina)

            resultado=float(x)*1000
            print(f'{x} KM equivale a {resultado} M')

        elif medida=='E':
            x=input('Digite o valor: ')
            v.valida_4(x,medida,pagina)

            resultado=float(x)/40000
            print(f'{x} KM equivale a {resultado} Voltas ao Mundo')

        elif medida=='F':
            x=input('Digite o valor: ')
            v.valida_4(x,medida,pagina)

            resultado=float(x)*9.46
            print(f'{x} Ano-Luz equivale a {resultado} Trilhões de KM')

        else:
            print('OPÇÃO INVÁLIDA!')
            medida_conv = str(input('Digite a opção correspondente: '))
            medida = medida_conv.upper()
            conv_medidas(medida,pagina)

    elif pagina==3:
        if medida=='G':
            pagina=2
            d.descreve_medidas(pagina)
            medida_conv = str(input('Digite a opção correspondente: '))
            medida = medida_conv.upper()
            conv_medidas(medida,pagina)

        elif medida=='A':
            x=input('Digite o valor: ')
            v.valida_4(x,medida,pagina)

            resultado=(float(x)*40000)*1000
            print(f'{x} Voltas ao Mundo equivale a {resultado} M')

        elif medida=='B':
            x=input('Digite o valor: ')
            v.valida_4(x,medida,pagina)

            resultado=(float(x)*40000)
            print(f'{x} Voltas ao Mundo equivale a {resultado} KM')

        elif medida=='C':
            x=input('Digite o valor: ')
            v.valida_4(x,medida,pagina)

            resultado=(float(x)*40000)/300000
            print(f'{x} Voltas ao Mundo equivale a {resultado} Segundos-Luz')

        elif medida=='D':
            x=input('Digite o valor: ')
            v.valida_4(x,medida,pagina)

            resultado=float(x)*300000
            print(f'{x} Segundos-Luz equivale a {resultado} KM')

        elif medida=='E':
            x=input('Digite o valor: ')
            v.valida_4(x,medida,pagina)

            resultado=(float(x)/40000)*300000
            print(f'{x} Segundos-Luz equivale a {resultado} Voltas ao Mundo')

        elif medida=='F':
            print('A Titulo de Curiosidade, o Universo Observável possui 45,66 bilhões de anos luz de raio e 91,32 bilhões de diâmetro!')
            print('Atualmente a Idade considerada do Universo é de 13,8 Bilhões de Anos-Luz:')
            print('Isso resulta em aproximadamente 130,5 Sexilhões de KM daqui da Terra até a borda ficticia do Universo.')
    
        else:
            print('OPÇÃO INVÁLIDA!')
            medida_conv = str(input('Digite a opção correspondente: '))
            medida = medida_conv.upper()
            conv_medidas(medida,pagina)

    sys.exit()