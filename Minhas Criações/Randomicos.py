import random  # necessário para utilizar o módulo random
import FuncRandom as f

random.seed()

quant = int(input('Quantos Números você deseja gerar? '))
x = int(input('De 0 até qual valor? '))
print(f.gerarnumero(x,quant))

print('')
quant = int(input('Quantas Letras você deseja gerar? '))
lista = []

for i in range (0,quant):
    letra = f.gerarletra()
    lista.append(letra)

print(lista)