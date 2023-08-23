import sys
import Descricao as d
import Valida as v
from time import sleep

def sistema(cad_ids,cad_nomes,cad_idades,cad_fones):
    d.menu()
    escolha=input('Digite a opção correspondente: ').upper()
    if escolha=='A':
        cadastro(cad_ids,cad_nomes,cad_idades,cad_fones)
    elif escolha=='B':
        consultar(cad_ids,cad_nomes,cad_idades,cad_fones)
    elif escolha=='C':
        senha = input('Digite a senha: ')
        if senha=='adm123':
            print('SENHA CORRETA, Aguarde estamos abrindo o banco de dados...')
            sleep(4)
            listagem(cad_ids,cad_nomes,cad_idades,cad_fones)
        else:
            print('ACESSO NEGADO: SENHA INCORRETA!')
            sleep(2)
    sistema(cad_ids,cad_nomes,cad_idades,cad_fones)

def cadastro(cad_ids,cad_nomes,cad_idades,cad_fones):
    valid=False
    while valid==False:
        nome = input('Digite seu nome: ').upper()
        valid=v.valida_nome(nome)

    valid=False
    while valid==False:
        idade = input('Digite sua idade: ')
        valid=v.valida_idade(idade)
    
    valid=False
    while valid==False:
        fone = input('Digite seu número de telefone: ')
        valid=v.valida_fone(fone)


    cad_ids.append(len(cad_ids))
    cad_nomes.append(nome)
    cad_idades.append(idade)
    cad_fones.append(fone)
    edicao(cad_ids,cad_nomes,cad_idades,cad_fones)
    print('')
    return cad_ids,cad_nomes,cad_idades,cad_fones
        
def edicao(cad_ids,cad_nomes,cad_idades,cad_fones):
    opcao=''
    valid=False
    d.confere_dados(cad_ids,cad_nomes,cad_idades,cad_fones)
    while opcao!='A' and opcao!='B' and opcao!='C' and opcao!='D':
        opcao = input('Digite a opção correspondente: ').upper()
    if opcao=='A':
        while valid==False:
            novo_nome = input('Digite seu nome: ').upper()
            valid=v.valida_nome(novo_nome)
        del cad_nomes[len(cad_nomes)-1]
        cad_nomes.append(novo_nome)
    elif opcao=='B':
        while valid==False:
            nova_idade = input('Digite sua idade: ')
            valid=v.valida_idade(nova_idade)
        del cad_idades[len(cad_idades)-1]
        cad_idades.append(nova_idade)
    elif opcao=='C':
        while valid==False:
            novo_fone = input('Digite seu número de telefone: ')
            valid=v.valida_fone(novo_fone)
        del cad_fones[len(cad_fones)-1]
        cad_fones.append(novo_fone)
    elif opcao=='D':
        return cad_ids,cad_nomes,cad_idades,cad_fones
    
    edicao(cad_ids,cad_nomes,cad_idades,cad_fones)

def consultar(cad_ids,cad_nomes,cad_idades,cad_fones):
    d.consulta_usuarios()
    opcao=''
    while opcao not in ['A','B']:
        opcao = input('Digite a opção correspondente: ').upper()
    pesquisa=''
    if opcao=='A':
        while not pesquisa.isdigit():
            pesquisa = input('Digite o ID do usuário: ')
        int_pesquisa = int(pesquisa)

        if int_pesquisa in cad_ids:
            posicao = cad_ids.index(int_pesquisa)
            print(f'ID: {cad_ids[posicao]}')
            print(f'NOME: {cad_nomes[posicao]}')
            print(f'IDADE: {cad_idades[posicao]}')
            print(f'TELEFONE: {cad_fones[posicao]}')
        else:
            print("Essa ID não está cadastrada!")

    elif opcao=='B':
        pesquisa = input('Digite o Nome do usuário: ').upper()
        if pesquisa in cad_nomes:
            posicao = cad_nomes.index(pesquisa)
            print(f'ID: {cad_ids[posicao]}')
            print(f'NOME: {cad_nomes[posicao]}')
            print(f'IDADE: {cad_idades[posicao]}')
            print(f'TELEFONE: {cad_fones[posicao]}')
        else:
            print('Nome não localizado no banco de dados!')

def listagem(cad_ids,cad_nomes,cad_idades,cad_fones):
    print('='*50+' BANCO DE DADOS USUÁRIOS '+'='*50)
    print(f'IDS => {cad_ids}')
    print(f'NOMES => {cad_nomes}')
    print(f'IDADES => {cad_idades}')
    print(f'TELEFONES => {cad_fones}')
    print('='*50)
    input('Lista gerada com sucesso, pressione ENTER para voltar ao menu...')