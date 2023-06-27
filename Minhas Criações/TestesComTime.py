from time import sleep

COLUNAS = 30
CARREGAR = "Carregando próximo teste..."

print ('Iniciando Primeiro Teste aguarde...')
sleep(4)
print("="*COLUNAS+" Iniciando contagem de 1 até 20 "+"="*COLUNAS)
sleep(3)

for i in range(0,20):
    print(i+1)
    sleep(0.3)

print ('')
print(CARREGAR)
sleep(2)

print('')
print("="*COLUNAS+" ACELERANDO UM CARRO "+"="*COLUNAS)
sleep(2)

print('')
v_max = int(input('Digite uma velocidade maxima em KM/H que seu carro aguenta ir: '))
print('O Carro andará em uma via onde todos transitam até 80km/h')
print('Iniciando o Teste...')
sleep(6)

print('')
for v_atual in range (0,v_max,+1):
    if v_atual == 80:
        print(f'{v_atual} KM/H')
        print ('Você está acima da velocidade MAX Permitida, acelerando lentamente...')
        sleep(3)
    elif v_atual > 80 and v_atual < 100:
        print (f'{v_atual} KM/H (acelerando lentamente...)')
        sleep(0.5)
    else:
        if v_atual == 100:
            print ('VOCÊ ACABOU COM SEU MOTOR IMPOSSIVEL CONTINUAR')
            v_atual = v_max    # Aqui estou fazendo um EXCEPTION interrompendo o FOR de continuar
        else:
            print(f'{v_atual} KM/H')
            sleep(0.2)

print ('')
print(CARREGAR)
sleep(2)

print('')
print("="*COLUNAS+" RADAR A CAMINHO "+"="*COLUNAS)
sleep(3)
print ('Você está acelerando seu carro quando de repente passa por um radar de 60km/h...')
sleep(5)

v_atual = 40
for v_atual in range (40,120,+2):
    if v_atual == 110:
        print(f'{v_atual} KM/H')
        print ('RADAR a caminho, diminua a velocidade...')
        sleep(3)
        for v_atual in range (110,54,-2):
            if v_atual == 56:
                print(f'{v_atual} KM/H')
                print ('Passando pelo Radar...')
                sleep(4)
                print ('Pode acelerar')
                sleep(2)
                for v_atual in range (56,120,+2):
                    print(f'{v_atual} KM/H')
                    sleep(0.3)
            else:
                print(f'{v_atual} KM/H')
                sleep(0.3)    
    else:
        print(f'{v_atual} KM/H')
        sleep(0.3)

print('')
print('Teste Concluido!')




# soma  = 0
# fim = int(input('Digite quantos números deseja somar: '))
# for i in range(0,fim):
#     numero = int(input('digite um valor: '))
#     soma += numero
# print(f'A soma dos números foi: {soma}')
