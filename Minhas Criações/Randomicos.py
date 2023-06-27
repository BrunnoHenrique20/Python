import random  # necessário para utilizar o módulo random

def gerarletra():
    letra_aleatoria = chr(random.randint(65, 90))  # Gera um número aleatório entre 65 e 90 (código ASCII para A e Z)    
    return letra_aleatoria

def gerarnumero(x,quant):
    numero_aleatorio = random.sample(range(x), k=quant)
    return numero_aleatorio

random.seed()

quant = int(input('Quantos Números você deseja gerar? '))
x = int(input('De 0 até qual valor? '))
print(gerarnumero(x,quant))

print('')
cont = int(input('Quantas Letras você deseja gerar? '))
lista = []

for i in range (0,cont):
    letra = gerarletra()
    lista.append(letra)

print(lista)