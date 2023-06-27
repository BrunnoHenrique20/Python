import random

def gerarletra():
    letra_aleatoria = chr(random.randint(65, 90))  # Gera um número aleatório entre 65 e 90 (código ASCII para A e Z)    
    return letra_aleatoria

def gerarnumero(x,quant):
    numero_aleatorio = random.sample(range(x), k=quant)
    return numero_aleatorio

def gerarnumero_range(x,y,quant):
    numero_aleatorio = random.sample(range(x,y), k=quant)
    return numero_aleatorio