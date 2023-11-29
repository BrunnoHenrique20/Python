from time import sleep
import Descricao as d
import Valida as v
# Importando os métodos que existem dentro dos arquivos Descricao.py e Valida.py
# Eles precisam estar na mesma pasta para funcionar corretamente
# Para não ter que digitar Descricao.nomedométodo nós colocamos um "alias" ou seja acessamos d.nomedométodo
# Apenas uma forma de tornar o código mais prático


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

    # Vai Repetir novamente o método caso nem A nem B nem C for digitado
    sistema(cad_ids,cad_nomes,cad_idades,cad_fones)


def cadastro(cad_ids,cad_nomes,cad_idades,cad_fones):

    # Trabalhando com chaves lógicas Boolean
    valid=False
    while valid==False:
        nome = input('Digite seu nome: ').upper()  # O Upper já vai salvar o nome todo em letras maiúsculas
        valid=v.valida_nome(nome, cad_nomes)

    valid=False
    while valid==False:
        idade = input('Digite sua idade: ')
        valid=v.valida_idade(idade)
    
    valid=False
    while valid==False:
        fone = input('Digite seu número de telefone: ')
        valid=v.valida_fone(fone)

    # Vai adicionar tudo que foi digitado nome,idade,fone as listas de cadastro (no final da lista)
    cad_ids.append(len(cad_ids))
    # O len(cad_ids) verifica a quantidade de itens salvos dentro de cad_ids
    # Se não tem nenhum cadastro então o primeiro ID vai ser 0
    # Se já tem 2 cadastros então o próximo ID selecionado vai ser 2 porque já tem o ID 0 e 1

    cad_nomes.append(nome)
    cad_idades.append(idade)
    cad_fones.append(fone)

    # Vai para o método de Edição caso a pessoa deseja alterar alguma informação que ele digitou
    edicao(cad_ids,cad_nomes,cad_idades,cad_fones)
    print('')
    return cad_ids,cad_nomes,cad_idades,cad_fones


def edicao(cad_ids,cad_nomes,cad_idades,cad_fones):
    opcao=''
    valid=False
    d.confere_dados(cad_ids,cad_nomes,cad_idades,cad_fones)
    # Descrição dos Dados informados!

    while opcao!='A' and opcao!='B' and opcao!='C' and opcao!='D':
        opcao = input('Digite a opção correspondente: ').upper()  # UPPER caso a = A

    if opcao=='A':
        while valid==False:
            novo_nome = input('Digite o novo nome: ').upper()
            valid=v.valida_nome(novo_nome, cad_nomes)

        # Vai remover o último nome adicionado na lista cad_nomes
        # O (-1) é porque vai verificar a quantidade de itens e vai voltar para o último nome adicionado
        # É justamente para impedir um BUGG de deletar informação em BRANCO
        del cad_nomes[len(cad_nomes)-1]

        # Agora que o nome antigo foi deletado do cadastro, ele vai adicionar o novo_nome digitado
        cad_nomes.append(novo_nome)

    elif opcao=='B':
        while valid==False:
            nova_idade = input('Digite a nova idade: ')
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
        # SALVAR DADOS!
        return cad_ids,cad_nomes,cad_idades,cad_fones

    # Vai entrar no método edição para mostrar na tela os dados novamente alterados para o usuário
    # Aqui só vai ser acessado após o usuário ter alterado algum nome,idade,fone
    # A única forma de sair do método edição é digitando a OPÇÃO D para salvar os dados! 
    edicao(cad_ids,cad_nomes,cad_idades,cad_fones)


def consultar(cad_ids,cad_nomes,cad_idades,cad_fones):
    d.consulta_usuarios()
    opcao=''

    while opcao not in ['A','B']:
        opcao = input('Digite a opção correspondente: ').upper()
    
    pesquisa=''
    # Vai precisar definir a variável com valor vazio antes justamente porque vai utilizar o WHILE
    # É obrigatório que uma variável já contenha algum valor se for usar no WHILE

    # Consultar por ID!
    if opcao=='A':

        # Enquanto a variável pesquisa não for todos os carácteres numéricos digitados
        while not pesquisa.isdigit():
            pesquisa = input('Digite o ID do usuário: ')
        
        # Convertendo o que foi digitado para inteiro ('123' = 123)
        int_pesquisa = int(pesquisa)

        # Se o ID estiver dentro da lista cad_ids
        # A variável posição é quem vai procurar pelos dados do usuário de acordo com o ID que foi cadastrado
        if int_pesquisa in cad_ids:
            posicao = cad_ids.index(int_pesquisa)
            print(f'ID: {cad_ids[posicao]}')
            print(f'NOME: {cad_nomes[posicao]}')
            print(f'IDADE: {cad_idades[posicao]}')
            print(f'TELEFONE: {cad_fones[posicao]}')
        else:
            print("Essa ID não está cadastrada!")

    # Agora a variável posição vai procurar filtrando pelo nome do usuário que foi cadastrado!
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


# Lista com Todos os dados cadastrados no Sistema! (APENAS O ADM TEM ACESSO)
def listagem(cad_ids,cad_nomes,cad_idades,cad_fones):
    print('='*50+' BANCO DE DADOS '+'='*50)
    print(f'IDS => {cad_ids}')
    print(f'NOMES => {cad_nomes}')
    print(f'IDADES => {cad_idades}')
    print(f'TELEFONES => {cad_fones}')

    # Vai imprimir o símbolo = 50 vezes
    print('='*50)

    # O input vazio sem variável serve apenas para dar uma pausa até que o usuário pressione ENTER
    input('Lista gerada com sucesso, pressione ENTER para voltar ao menu...')
    