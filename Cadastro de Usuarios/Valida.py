
# Método responsável por retornar o valor do valid lá no arquivo Funcoes.py
def valida_nome(nome, cad_nomes):
    if len(nome)==0:
        print('O campo não pode estar vazio!')
        return False
    elif len(nome)>20:
        print('Nome muito grande! (MAX caracteres permitidos: 20)')
        return False
    elif nome.isnumeric():
        print('Números não são permitidos!')
        return False
    
    # Vai verificar se o nome digitado já existe dentro do cadastro nome
    elif nome in cad_nomes:
        print('Desculpe, já existe um usuário cadastrado com esse nome')
        return False
    else:
        return True


def valida_idade(idade):
    if len(idade)==0:
        print('O campo não pode estar vazio!')
        return False
    elif int(idade)>100:
        print('A idade não pode ser maior do que 100 anos!')
        return False
    elif not idade.isdecimal():
        print('Letras e caracteres especiais não são permitidos!')
        return False
    else:
        return True


def valida_fone(fone):
    if len(fone)==0:
        print('O campo não pode estar vazio!')
        return False
    elif len(fone)>11:
        print('Numero de Telefone grande demais! (MAX Permitido: 11 digitos)')
        return False
    elif not fone.isdecimal():
        print('Letras e caracteres especiais não são permitidos!')
        return False
    else:
        return True