import Descricao as d

def calc_bingo(sorteados:float,marcados:float):
    total=75-sorteados
    cartela=25-marcados
    prob=float("{:.2f}".format((cartela/total)*100))
    return prob

def valida_sorteados(sorteados:float):
    if sorteados>74:
        print('ERRO: Impossivel sortear acima de 75 numeros!')
    elif sorteados==75:
        print('ERRO: Não é possivel calcular uma probabilidade sendo que todos os 75 numeros foram sorteados, digite um valor menor!')
    else:
        return True
    return False

def valida_marcados(sorteados:float,marcados:float):
    if marcados>25:
        print('ERRO: Você digitou mais números do que existem na cartela (MAX: 25)!')
    elif marcados==25:
        print('ERRO: Com 25 numeros marcados você já é o ganhador do Bingo, digite um número menor')
    if marcados>sorteados:
        print('ERRO: A quantidade de números marcados é maior do que a quantidade que foi sorteada, não é possível calcular!')
    else:
        return True
    return False

def acertos_consecutivos():
    validar=False
    while validar==False:
        odd=''
        while odd.isdigit()==False:
            odd = input('Digite o valor da ODD a ser calculada: ')
        validar=verificavalor(odd)

    validar=False
    while validar==False:
        apostas=''
        while apostas.isdigit()==False:
            apostas = input('Digite o numero de Apostas consecutivas: ')
        validar=verificavalor(apostas)

    odd_x=float(odd)
    apostas_x=float(apostas)
    p_conv = 100/odd_x
    p = p_conv/100
    count = 1

    print('-'*50)
    while count <= apostas_x :
        p_total = p**count
        p_final = p_total*100
        print('Acertos '+str(count)+'/'+apostas+' = %.2f'%(p_final)+' %')
        count += 1
    print('-'*50)

def riscobaixo_E():
    d.descrevebaixo_E()

    validar=False
    while validar==False:
        capital=''
        while capital.isdigit()==False:
            capital= input('Defina seu capital total: ')
        validar=verificacapital(capital)
    
    validar=False
    while validar==False:
        qtd=''
        while qtd.isdigit()==False:
            qtd= input('Quantas apostas você deseja fazer com esse valor? ')
        validar=verificaQTD(qtd)

    capital_x=float(capital)
    qtd_x=float(qtd)
    aposta=int(capital_x/qtd_x)
    sequencia=1
    lucro=0.00
    total_apostado=0.00
    print('')
    print('| SEQUÊNCIA |  APOSTA  |  GANHOS  |   LUCRO  | TOTAL APOSTADO |')

    while sequencia<=qtd_x:
        ganhos=aposta*36
        total_apostado=total_apostado+aposta
        lucro=ganhos-total_apostado
        print(f'| {sequencia:>8}º | {aposta:8.2f} | {ganhos:8.2f} | {lucro:8.2f} | R$ {total_apostado:11.2f} |')
        sequencia+=1

def riscomedio_E():
    d.descrevemedio_E()

    validar=False
    while validar==False:
        capital=''
        while capital.isdigit()==False:
            capital= input('Defina seu capital total: ')
        validar=verificacapital(capital)

    capital_x=float(capital)
    sequencia=0
    aposta=0.00
    ganhos=aposta*36.00
    total_apostado=0.00
    lucro=0.00
    print('')
    print('| SEQUÊNCIA |  APOSTA  |  GANHOS  |   LUCRO  | TOTAL APOSTADO |')
    
    while total_apostado<=capital_x and lucro>=-20:
        sequencia+=1
        if lucro<1:
            aposta+=1.00
            ganhos=aposta*36
            total_apostado=total_apostado+aposta
            lucro=ganhos-total_apostado
        else:
            total_apostado=total_apostado+aposta
            lucro=ganhos-total_apostado
        print(f'| {sequencia:>8}º | {aposta:8.2f} | {ganhos:8.2f} | {lucro:8.2f} | R$ {total_apostado:11.2f} |')

def riscoalto_E():
    d.descrevealto_E()

    validar=False
    while validar==False:
        capital=''
        while capital.isdigit()==False:
            capital= input('Defina seu capital total: ')
        validar=verificacapital(capital)

    capital_x=float(capital)
    sequencia=0
    aposta=0.50
    ganhos= aposta*36.00
    total_apostado=0.00
    lucro=1.00
    print('')
    print('| SEQUÊNCIA |  APOSTA  |  GANHOS  |   LUCRO  | TOTAL APOSTADO |')
    
    while total_apostado<=capital_x and lucro>=-20:
        sequencia+=1
        aposta+=0.50
        if lucro<1:
            aposta+=1.00
        ganhos=aposta*36
        total_apostado=total_apostado+aposta
        lucro=ganhos-total_apostado
        print(f'| {sequencia:>8}º | {aposta:8.2f} | {ganhos:8.2f} | {lucro:8.2f} | R$ {total_apostado:11.2f} |')

def riscobaixo_F():
    d.descrevebaixo_F()

    validar=False
    while validar==False:
        capital=''
        while capital.isdigit()==False:
            capital= input('Defina seu capital total: ')
        validar=verificacapital(capital)
    
    validar=False
    while validar==False:
        qtd=''
        while qtd.isdigit()==False:
            qtd= input('Quantas apostas você deseja fazer com esse valor? ')
        validar=verificaQTD(qtd)

    capital_x=float(capital)
    qtd_x=float(qtd)
    aposta=int(capital_x/qtd_x)
    sequencia=1
    lucro=0.00
    total_apostado=0.00
    odd=2.00
    print('')
    print('| SEQUÊNCIA |  APOSTA  |  GANHOS  |   LUCRO  | TOTAL APOSTADO | SAÍDA AUTOMÁTICA EM |')

    while sequencia<=qtd_x:
        ganhos=aposta*odd
        total_apostado=total_apostado+aposta
        lucro=ganhos-total_apostado
        print(f'| {sequencia:>8}º | {aposta:8.2f} | {ganhos:8.2f} | {lucro:8.2f} | R$ {total_apostado:11.2f} | x{odd:18.2f} |')
        sequencia+=1
        odd+=1

def riscomedio_F():
    d.descrevemedio_F()

    validar=False
    while validar==False:
        capital=''
        while capital.isdigit()==False:
            capital= input('Defina seu capital total: ')
        validar=verificacapital(capital)
    
    validar=False
    while validar==False:
        odd=''
        while odd.isdigit()==False:
            odd= input('Defina uma ODD Fixa que deseja sair automaticamente: ')
        validar=verificaQTD(odd)
    
    capital_x=float(capital)
    odd_x=float(odd)
    aposta=0.10
    lucro=0.00
    total_apostado=0.00
    sequencia=1
    print('')
    print('| SEQUÊNCIA |  APOSTA  |  GANHOS  |   LUCRO  | TOTAL APOSTADO | SAÍDA AUTOMÁTICA EM |')

    while total_apostado<=capital_x and lucro>=-20:
        posicao = fibonacci(sequencia)
        aposta = posicao[sequencia - 1] * 0.1 # numero de fibonacci
        ganhos=aposta*odd_x
        total_apostado=total_apostado+aposta
        lucro=ganhos-total_apostado
        print(f'| {sequencia:>8}º | {aposta:8.2f} | {ganhos:8.2f} | {lucro:8.2f} | R$ {total_apostado:11.2f} | x{odd_x:18.2f} |')
        sequencia+=1
        
def riscoalto_F():
    d.descrevealto_F()
    
    validar=False
    while validar==False:
        capital=''
        while capital.isdigit()==False:
            capital= input('Defina seu capital total: ')
        validar=verificacapital(capital)

    capital_x=float(capital)
    odd=10.00
    aposta=0.10
    lucro=0.00
    total_apostado=0.00
    sequencia=1
    print('')
    print('| SEQUÊNCIA |  APOSTA  |  GANHOS  |   LUCRO  | TOTAL APOSTADO | SAÍDA AUTOMÁTICA EM |')

    while total_apostado<=capital_x and lucro>=-20:
        posicao = fibonacci(sequencia)
        aposta = posicao[sequencia - 1] * 0.1 # numero de fibonacci
        ganhos=aposta*odd
        total_apostado=total_apostado+aposta
        lucro=ganhos-total_apostado
        print(f'| {sequencia:>8}º | {aposta:8.2f} | {ganhos:8.2f} | {lucro:8.2f} | R$ {total_apostado:11.2f} | x{odd:18.2f} |')
        sequencia+=1
        if odd==3.00:
            pass
        else:
            odd=odd-0.5

def riscoalto_G():
    d.descrevealto_G()
    
    validar=False
    while validar==False:
        capital=0
        while capital.isdigit()==False:
            capital= input('Defina seu capital total: ')
        validar=verificacapital(capital)

    capital_x=float(capital)
    odd=14.00
    aposta=0.01
    lucro=0.00
    total_apostado=0.00
    sequencia=1
    print('')
    print('| SEQUÊNCIA |  APOSTA  |  GANHOS  |   LUCRO  | TOTAL APOSTADO | MULT DO BRANCO |')

    while total_apostado<=capital_x and lucro>=0:
        posicao = fibonacci(sequencia)
        aposta = posicao[sequencia - 1] * 0.01 # numero de fibonacci
        ganhos=aposta*odd
        total_apostado=total_apostado+aposta
        lucro=ganhos-total_apostado
        print(f'| {sequencia:>8}º | {aposta:8.2f} | {ganhos:8.2f} | {lucro:8.2f} | R$ {total_apostado:11.2f} | x{odd:18.2f} |')
        sequencia+=1

def riscobaixo_G():
    d.descrevebaixo_G()
    capital = float(se_capital_alto(0))
    odd=14.00
    aposta=0.01
    lucro=0.00
    total_apostado=0.00
    sequencia=1
    print('')
    print('| SEQUÊNCIA |  APOSTA  |  GANHOS  |   LUCRO  | TOTAL APOSTADO | MULT DO BRANCO |')

    while total_apostado<=capital:
        ganhos=aposta*odd
        total_apostado=total_apostado+aposta
        lucro=ganhos-total_apostado
        print(f'| {sequencia:>8}º | {aposta:8.2f} | {ganhos:8.2f} | {lucro:8.2f} | R$ {total_apostado:11.2f} | x{odd:18.2f} |')
        sequencia+=1
        if lucro<0:
            aposta=aposta*2

def riscomedio_G():
    d.descrevemedio_G()
    capital = float(se_capital_alto(0))
    odd=14.00
    aposta=0.01
    lucro=0.00
    total_apostado=0.00
    sequencia=1
    print('')
    print('| SEQUÊNCIA |  APOSTA  |  GANHOS  |   LUCRO  | TOTAL APOSTADO | MULT DO BRANCO |')

    while total_apostado<=capital:
        ganhos=aposta*odd
        total_apostado=total_apostado+aposta
        lucro=ganhos-total_apostado
        print(f'| {sequencia:>8}º | {aposta:8.2f} | {ganhos:8.2f} | {lucro:8.2f} | R$ {total_apostado:11.2f} | x{odd:18.2f} |')
        sequencia+=1
        if aposta<0.20:
            aposta+=0.01
        elif aposta>=0.20 and aposta<0.40:
            aposta+=0.02
        elif aposta>=0.40 and aposta<1.00:
            aposta+=0.05
        elif aposta>=1.00 and aposta<1.20:
            aposta+=0.20
        elif aposta>=1.20 and aposta<2.00:
            aposta+=0.10
        elif aposta>=2 and aposta<3:
            aposta+=0.20
        elif aposta>=3 and aposta<10:
            aposta+=0.50
        elif aposta>=10 and aposta<40:
            aposta+=2.00
        elif aposta>=40 and aposta<100:
            aposta+=5.00
        elif aposta>=100 and aposta<170:
            aposta+=10
        elif aposta>=170 and aposta<200:
            aposta+=30
        elif aposta>=200 and aposta<1000:
            aposta+=50
        elif aposta>=1000 and aposta<2000:
            aposta+=100
        else:
            aposta+=500

def se_capital_alto(montante):
    chave=False
    while chave==False:
        montante= input('Defina seu capital total: ')
        if montante.isdigit()==True:
            chave=True

    while float(montante)<1 or float(montante)>150000:
        print('Desculpe, essa estratégia está LIMITADA a um valor máximo de R$ 150.000 digite um valor menor!')
        print('(MIN: R$ 1 | MAX: R$ 150.000)')
        montante= input('Defina seu capital total: ')

    return montante

def fibonacci(n):
    fib_lista = [1, 2]

    while len(fib_lista) < n:
        proximo_termo = fib_lista[-1] + fib_lista[-2]
        fib_lista.append(proximo_termo)

    return fib_lista

def verificavalor(valor):
    if float(valor)>100:
        print('ERRO: Digite um valor menor! (MAX: 100)')
        chave=False
    elif float(valor)<0:
        print('ERRO: Valores negativos não são permitidos!')
        chave=False
    elif float(valor)>=0 and float(valor)<=1:
        print('ERRO: Digite um valor maior do que 1!')
        chave=False
    else:
        chave=True
    
    return chave

def verificacapital(valor):
    if float(valor)>150000:
        print('ERRO: Digite um valor menor! (MAX: R$ 150.000,00)')
        chave=False
    elif float(valor)<0:
        print('ERRO: Valores negativos não são permitidos!')
        chave=False
    elif float(valor)>=0 and float(valor)<0.5:
        print('ERRO: Digite um valor maior! (MIN: R$ 0,50)')
        chave=False
    else:
        chave=True
    
    return chave

def verificaQTD(valor):
    if float(valor)>1000:
        print('ERRO: Digite um valor menor! (MAX: 1000)')
        chave=False
    elif float(valor)<1:
        print('ERRO: Digite um valor válido!')
        chave=False
    else:
        chave=True
    
    return chave