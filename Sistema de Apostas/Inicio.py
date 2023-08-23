# EM CONSTRUÇÃO
import sys
import Descricao as d
import Valida as v

def iniciar(opc,apc):
    d.menu()
    while opc not in ['A','B','C','D','E','F','G','H','I','J','K','L']:
        opc=input('Digite a opção correspondente: ').upper()
    if opc=='A':
        v.acertos_consecutivos()
    elif opc=='B':
        d.blackjack()
    elif opc=='C':
        d.odd_prob()

    elif opc=='D':
        d.menu_risco()
        while apc not in ['A','B','C']:
            apc=input('Digite a opção correspondente: ').upper()
        if apc=='A':
            d.placar_multiplo_A()
        elif apc=='B':
            d.placar_multiplo_B()
        elif apc=='C':
            d.placar_multiplo_C()

    elif opc=='E':
        d.menu_risco()
        while apc not in ['A','B','C']:
            apc=input('Digite a opção correspondente: ').upper()
        if apc=='A':
            v.riscoalto_E()
        elif apc=='B':
            v.riscomedio_E()
        elif apc=='C':
            v.riscobaixo_E()
            
    elif opc=='F':
        d.menu_risco()
        while apc not in ['A','B','C']:
            apc=input('Digite a opção correspondente: ').upper()
        if apc=='A':
            v.riscoalto_F()
        elif apc=='B':
            v.riscomedio_F()
        elif apc=='C':
            v.riscobaixo_F()

    elif opc=='G':
        d.menu_risco()
        while apc not in ['A','B','C']:
            apc=input('Digite a opção correspondente: ').upper()
        if apc=='A':
            v.riscoalto_G()
        elif apc=='B':
            v.riscomedio_G()
        elif apc=='C':
            v.riscobaixo_G()

    elif opc=='H':
        d.lightdice()
    elif opc=='I':
        d.menu_futebol()
        while apc not in ['A','B','C','D','E','F','G']:
            apc=input('Digite a opção correspondente: ').upper()
        if apc=='A':
            d.menu_futebol_A()
        elif apc=='B':
            d.menu_futebol_B()
        elif apc=='C':
            d.menu_futebol_C()
        elif apc=='D':
            d.menu_futebol_D()
        elif apc=='E':
            d.menu_futebol_E()
        elif apc=='F':
            d.menu_futebol_F()
        elif apc=='G':
            d.menu_futebol_G()

    elif opc=='J':
        d.rumo_partida()
    elif opc=='K':
        d.bingo()
        chave1,chave2=False,False
        while chave1==False:
            sorteados=''
            while sorteados.isdigit()==False:
                sorteados=input('Digite a quantidade de números sorteados: ')
            chave1 = v.valida_sorteados(float(sorteados))
        while chave2==False:
            marcados=''
            while marcados.isdigit()==False:
                marcados=input('Digite a quantidade de números marcados na cartela: ')
            chave2 = v.valida_marcados(float(sorteados),float(marcados))
        resultado = v.calc_bingo(float(sorteados),float(marcados))
        print('')
        print(f'A Probabilidade de ter o próximo número sorteado marcado é de {resultado} %')
        print('')

    elif opc=='L':
        sys.exit()
    input('...ROLE a Tela ou Pressione ENTER para voltar ao menu...')
    iniciar('','')

iniciar('','')