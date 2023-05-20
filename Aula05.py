idade = int(input('Digite sua idade: '))

if idade > 60:
    print('Você pode se aposentar!')
elif idade >= 18:
    print('Você é maior de idade e precisa trabalhar para depois aposentar!')
elif idade >= 0:
    print('Você é muito novo ainda!')
else:
    print('Você nem nasceu ainda!')