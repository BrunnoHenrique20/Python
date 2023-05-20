x = int(input('Primeiro Numero: '))
y = int(input('Segundo Numero: '))
operacao = input('Qual operação: ')

if operacao != 'somar':
    if operacao != 'subtrair':
        if operacao != 'multiplicar':
            if operacao != 'dividir':
                print('OPERAÇÃO INVÁLIDA Digite somar, subtrair, multiplicar ou dividir!')
                operacao = input('Qual operação: ')

if operacao == 'somar':
    resultado = x+y
elif operacao == 'subtrair':
    resultado = x-y
elif operacao == 'multiplicar':
    resultado = x*y
elif operacao == 'dividir':
    resultado = x/y

print("O resultado é: " + str(resultado))