# Implementar uma Regra para NÃO REPETIR números ja sorteados

import random
import FuncRandom as f
from time import sleep

print('='*30+'  INICIAR BINGO  '+'='*30)
sleep(3)
random.seed()

sorteio_ativo = 1
novo_sorteio = 'S'

while sorteio_ativo == 1:

    if novo_sorteio == 'N':
        sorteio_ativo = 0
        print('BINGO!!!')

    elif novo_sorteio == 'S':
        letra = f.gerarletra()

        if letra == 'B' or letra == 'I' or letra == 'N' or letra == 'G' or letra == 'O':
            if letra == 'B':
                numeral = f.gerarnumero_range(1,15,1)
                print(letra+' '+str(numeral))
            elif letra == 'I':
                numeral = f.gerarnumero_range(16,30,1)
                print(letra+' '+str(numeral))
            elif letra == 'N':
                numeral = f.gerarnumero_range(31,45,1)
                print(letra+' '+str(numeral))
            elif letra == 'G':
                numeral = f.gerarnumero_range(46,60,1)
                print(letra+' '+str(numeral))
            elif letra == 'O':
                numeral = f.gerarnumero_range(61,75,1)
                print(letra+' '+str(numeral))
                
            novo_sorteio = str(input('Sortear mais um Numero (S/N)? '))
            sleep(1)
        else:
            pass
    
