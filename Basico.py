a = 10
b = 15
c = a+b   # c recebe a=10 e b=15
a = 45    # a passa a valer 45
print(c)

'''
irá mostrar 25, ja que a soma permanece
com os valores antigos
'''

c = a-4
print(' - ' * 20)   # espaçamento um separador multiplicado 30 vezes
print(c)    # c já com os valores novos

''' as variáveis são case sensitive maiusculas diferentes das minusculas'''
''' ALT + SHIFT + F = Autoformatador de codigo para facilitar a visualização'''
''' ALT + S = Salvar Arquivo .PY '''

print(' - ' * 20)

nome = str('Brunno')
sobrenome = str('Henrique')
completo = nome + ' ' + sobrenome
print(completo) # Nome Completo

print(' - ' * 20)

idade = int(26)
idade2 = float(25.48)
print(idade)
print(idade2)

print(' - ' * 20)

ehverdade = True   # Ou pode utilizar testar = bool(True)
print(ehverdade)

print(' - ' * 20)

idade = 12
maiordeidade = idade >= 18

if maiordeidade:
    print('Pode dirigir')
else:
    print('De menor nao dirige...')    

print(' - ' * 20)

