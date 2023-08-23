def menu():
    print('='*40+' CADASTRO DE USUÁRIOS '+'='*40)
    print('')
    print('A => Cadastrar Novo Usuário')
    print('B => Consultar Usuário')
    print('C => Banco de Dados Usuários [ADM]')
    print('')

def confere_dados(cad_ids,cad_nomes,cad_idades,cad_fones):
    print('')
    print('---Confirme abaixo se os dados estão corretos---')
    print(f'ID: {cad_ids[len(cad_ids)-1]}')
    print(f'NOME: {cad_nomes[len(cad_nomes)-1]}')
    print(f'IDADE: {cad_idades[len(cad_idades)-1]}')
    print(f'TELEFONE: {cad_fones[len(cad_fones)-1]}')
    print('-'*30)
    print('A) => Editar Nome')
    print('B) => Editar Idade')
    print('C) => Editar Telefone')
    print('D) => Salvar')
    print('')

def consulta_usuarios():
    print('-'*50)
    print('A) => Pesquisar usuário por ID')
    print('B) => Pesquisar usuário por Nome')
    print('')