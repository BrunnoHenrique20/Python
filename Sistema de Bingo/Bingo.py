import random
import FuncRandom as f
import Descricao as d
import Validar as v
from time import sleep
import sys

sys.setrecursionlimit(5000)
recursao = f.minha_funcao_recursiva(1)

d.menu()
escolha=''
while escolha not in ['A','B']:
    escolha = input(str('Digite a opção correspondente: ')).upper()
f.escolher(escolha)
sys.exit()