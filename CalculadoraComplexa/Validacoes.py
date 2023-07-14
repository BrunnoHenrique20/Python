import Texto as d
import Funcoes
import ConversorMoedas, ConversorTemperatura, ConversorTempo, ConversorMedidas
from time import sleep


def valida_1(x,moeda):
    y = str(x)
    if y.isdecimal():
        valida=True
        x=float(x)
        if x==0:
            print('Não é possivel calcular um valor ZERADO!')
            sleep(2)
            ConversorMoedas.conv_moeda(moeda)
        elif x<0:
            print('Não é possivel calcular valores NEGATIVOS!')
            sleep(2)
            ConversorMoedas.conv_moeda(moeda)
    else:
        print('Letras e espaços vazios não são permitidos, digite apenas numeros!')
        sleep(2)
        ConversorMoedas.conv_moeda(moeda)

def valida_2(x,clima):
    y = str(x)
    if y.isdecimal():
        valida=True
        x=float(x)
    else:
        print('Letras e espaços vazios não são permitidos, digite apenas numeros!')
        sleep(2)
        ConversorTemperatura.conv_clima(clima)

def valida_3(x,time,pagina):
    y = str(x)
    if y.isdecimal():
        valida=True
        x=float(x)
        if x==0:
            print('Não é possivel calcular um tempo ZERADO!')
            sleep(2)
            ConversorTempo.conv_time(time,pagina)
        elif x<0:
            print('Não é possivel calcular um tempo NEGATIVO!')
            sleep(2)
            ConversorTempo.conv_time(time,pagina)
    else:
        print('Letras e espaços vazios não são permitidos, digite apenas numeros!')
        sleep(2)
        ConversorTempo.conv_time(time,pagina)

def valida_escolha(time:str, pagina:int):
    while len(time)==0 or len(time)>1 or time in ['M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','0','1','2','3','4','5','6','7','8','9']:
        time_conv = input('Digite a opção correspondente: ')
        time = time_conv.upper()
        ConversorTempo.conv_time(time,pagina)

    if time in ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'I', 'J']:
        x=input('Digite o valor: ')
        valida_3(x,time,pagina)

    if pagina==1:
        if time=='K':
            pagina=2
            d.descreve_time(pagina)
            time_conv = input('Digite a opção correspondente: ')
            time = time_conv.upper()
            ConversorTempo.conv_time(time,pagina)
        elif time=='L':
            time_conv = input('Digite a opção correspondente: ')
            time = time_conv.upper()
            ConversorTempo.conv_time(time,pagina)

    elif pagina==2:
        if time=='K':
            pagina=3
            d.descreve_time(pagina)
            time_conv = input('Digite a opção correspondente: ')
            time = time_conv.upper()
            ConversorTempo.conv_time(time,pagina)
        elif time=='L':
            pagina=1
            d.descreve_time(pagina)
            time_conv = input('Digite a opção correspondente: ')
            time = time_conv.upper()
            ConversorTempo.conv_time(time,pagina)

    elif pagina==3:
        if time=='K':
            pagina=2
            d.descreve_time(pagina)
            time_conv = input('Digite a opção correspondente: ')
            time = time_conv.upper()
            ConversorTempo.conv_time(time,pagina)
        elif time=='L':
            time_conv = input('Digite a opção correspondente: ')
            time = time_conv.upper()
            ConversorTempo.conv_time(time,pagina)
    return x

def valida_4(x,medida,pagina):
    y = str(x)
    if y.isdecimal():
        valida=True
        x=float(x)
        if x==0:
            print('Não é possivel calcular uma distancia ZERADA!')
            sleep(2)
            ConversorMedidas.conv_medidas(medida,pagina)
        elif x<0:
            print('Não é possivel calcular distancias NEGATIVAS!')
            sleep(2)
            ConversorMedidas.conv_medidas(medida,pagina)
    else:
        print('Letras e espaços vazios não são permitidos, digite apenas numeros!')
        sleep(2)
        ConversorMedidas.conv_medidas(medida,pagina)

def valida_quant(x):
    if x.isdecimal():
        x=int(x)
        if x>100:
            print('Você digitou uma quantidade muito grande, digite no máximo até 100 números!')
            print('')
            Funcoes.calculadora('L',1)
        elif x==0:
            print('ZERO não é uma quantidade válida!')
            print('')
            Funcoes.calculadora('L',1)
        elif x==1:
            print('Não é possível calcular a média de apenas um número!')
            print('')
            Funcoes.calculadora('L',1)
    else:
        print('Caracteres e espaços em brancos não são permitidos!')
        print('')
        Funcoes.calculadora('L',1)
    return x

def contem_float(x):
    try:
        z = float(x)
        return True
    except ValueError:
        return False

def is_number(x):
    if x.isdigit():  # Verifica se todos os caracteres são dígitos
        return True
    elif x[0] in ['+', '-'] and x[1:].isdigit():  # Verifica se há um sinal seguido por dígitos
        return True
    else:
        try:
            float(x)  # Tenta converter a string em um número float
            return True
        except ValueError:
            return False
