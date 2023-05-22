print('='*20+'EXPERIMENTOS BINOMIAIS'+'='*20)
print('')

n = int(input('Quantas apostas deseja fazer: '))
p_converte = float(input('Defina a probabilidade em porcentagem de acertar 1 aposta: '))
p = p_converte/100
x = int(input('Chance de X das '+str(n)+' apostas de acertarem:'))

n_fator=1
count=1

while count <= n:
    n_fator *= count
    count += 1

'''print(n_fator)'''

x_fator=1
count=1

while count <= x:
    x_fator *= count
    count += 1

'''print(x_fator)'''

calc1 = n-x
c_fator=1
count=1

while count <= calc1:
    x_fator *= count
    count += 1

'''print(c_fator)'''

resultado = n_fator / x_fator * c_fator * (p**x) * (1-p) ** calc1
r_final = resultado*100

print('')
print('A Probabilidade de '+str(x)+' das '+str(n)+' apostas ocorrerem é de '+str(r_final)+' %')