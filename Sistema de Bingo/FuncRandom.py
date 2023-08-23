import random
import sys
import Validar as v
from time import sleep

def minha_funcao_recursiva(numero):
    if numero <= 0:
        return 0
    return numero + minha_funcao_recursiva(numero - 1)

def gerarletra():
    letra_aleatoria = chr(random.randint(65, 90))  # Gera um número aleatório entre 65 e 90 (código ASCII para A e Z)    
    return letra_aleatoria

def gerarnumero(x,quant):
    numero_aleatorio = random.sample(range(x), k=quant)
    return numero_aleatorio

def gerarnumero_range(x,y,quant):
    numero_aleatorio = random.sample(range(x,y), k=quant)
    return numero_aleatorio

def gerar_letra():
    letra=''
    while letra!='B' and letra!='I' and letra!='N' and letra!='G' and letra!='O':
        letra = gerarletra().upper()
        
        if letra == 'B' or letra == 'I' or letra == 'N' or letra == 'G' or letra == 'O':
                return letra

def gerar_numeral(letra):
    if letra == 'B':
        numeral = gerarnumero_range(1,15,1)
    elif letra == 'I':
        numeral = gerarnumero_range(16,30,1)
    elif letra == 'N':
        numeral = gerarnumero_range(31,45,1)
    elif letra == 'G':
        numeral = gerarnumero_range(46,60,1)
    elif letra == 'O':
        numeral = gerarnumero_range(61,75,1)
    else:
        numeral = 0
    return numeral

def escolher(escolha):
    if escolha=='A':
        print('Aguarde, estamos gerando a sua cartela...')
        sleep(3)
        print('Sua cartela abaixo:')
        print('')
        gerarcartela(escolha,1,1)
    elif escolha=='B':
        qtd = input('Quantas cartelas deseja gerar? ')
        if qtd.isdigit():
            print('Aguarde, estamos gerando suas cartelas...')
            sleep(3)
            quant=int(qtd)
            gerarcartela(escolha,1,quant)
        else:
            escolher(escolha)

def gerarcartela(escolha,j,quant):
    lista1=[]
    lista2=[]
    lista3=[]
    lista4=[]
    lista5=[]

    minha_cartela=gerador(lista1,lista2,lista3,lista4,lista5)

    # CODIGO DE VERIFICACAO E LANCAR CARTELA
    lista1_v = v.tem_repeticao(lista1)
    lista2_v = v.tem_repeticao(lista2)
    lista3_v = v.tem_repeticao(lista3)
    lista4_v = v.tem_repeticao(lista4)
    lista5_v = v.tem_repeticao(lista5)

    if lista1_v==False and lista2_v==False and lista3_v==False and lista4_v==False and lista5_v==False:
        if j<10:
            print('-'*43+' Nº 00'+str(j))
        elif j>=10 and j<100:
            print('-'*43+' Nº 0'+str(j))
        else:
            print('-'*43+' Nº '+str(j))

        print(f'B => {lista1}')
        print(f'I => {lista2}')
        print(f'N => {lista3}')
        print(f'G => {lista4}')
        print(f'O => {lista5}')
        
        if j==quant and escolha=='A':
            game(minha_cartela)

        if j==quant and escolha=='B':
            print('')
            print('Suas cartelas foram geradas com sucesso!')
        else:
            sleep(0.5)
            gerarcartela(escolha,j+1,quant)
    else:
        gerarcartela(escolha,j,quant)


def gerador(lista1,lista2,lista3,lista4,lista5):
    letra=gerar_letra()
    numeral=gerar_numeral(letra)

    if letra=='B' or letra=='I' or letra=='N' or letra=='G' or letra=='O':
        for i in range(5):
            numeral=gerar_numeral('B')
            lista1.insert(i,numeral)
            
        for i in range(5):
            numeral=gerar_numeral('I')
            lista2.insert(i,numeral)
            
        for i in range(5):
            numeral=gerar_numeral('N')
            lista3.insert(i,numeral)

        for i in range(5):
            numeral=gerar_numeral('G')
            lista4.insert(i,numeral)
            
        for i in range(5):
            numeral=gerar_numeral('O')
            lista5.insert(i,numeral)
            
    lista1.sort(), lista2.sort(), lista3.sort(), lista4.sort(), lista5.sort()
    conjunto=lista1+lista2+lista3+lista4+lista5
    return conjunto

def game(minha_cartela):
    print('')
    input('PRESSIONE ENTER PARA INICIAR...')
    print('-'*50)
    numeros_sorteados=[]
    gerar_um(minha_cartela,numeros_sorteados)

def gerar_um(minha_cartela, numeros_sorteados):
    letra=gerar_letra()
    numeral=gerar_numeral(letra)

    if letra=='B':
        numeral=gerar_numeral('B')
    elif letra=='I':
        numeral=gerar_numeral('I')
    elif letra=='N':
        numeral=gerar_numeral('N')
    elif letra=='G':
        numeral=gerar_numeral('G')
    elif letra=='O':
        numeral=gerar_numeral('O')

    if numeral in numeros_sorteados:
        gerar_um(minha_cartela, numeros_sorteados)
    else:
        print('Sorteando uma nova bola...')
        sleep(3)
        print('-'*50)
        print('BOLA SORTEADA: '+letra+' '+str(numeral))

        if numeral in minha_cartela:
            minha_cartela.remove(numeral)
        
        numeros_sorteados.append(numeral)
        print(f'Minha Cartela: {minha_cartela}')
        print(f'Numeros Sorteados: {numeros_sorteados}')
        print('-'*50)

        if minha_cartela==[]:
            input('BINGO!!! VOCÊ GANHOU!!!')
            sys.exit()
        else:
            input('PRESSIONE ENTER PARA GERAR OUTRO NUMERO...')
            gerar_um(minha_cartela,numeros_sorteados)