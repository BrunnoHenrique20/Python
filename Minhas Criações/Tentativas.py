print('#' * 5 + ' Teste uma variável ' + '#' * 5)

tentativas = 5
while tentativas > 0:
    print (f'Tentativas: [{tentativas}]')
    aposta = int(input('Digite sua aposta: '))

    if aposta == 10:
        print("Acertou!")
        break
    else:
        tentativas = tentativas - 1
    print('-'*10)

if tentativas == 0:
    print ('Você Perdeu!')