print('='*20+'PROBABILIDADES DE ACERTOS'+'='*20)
print('')

apostas = 10
#apostas = int(input('Numero de Apostas: '))
odd = float(input('Digite a ODD: '))
p_conv = 100/odd
p = p_conv/100
count = 1

while count <= apostas :
    p_total = p**count
    p_final = p_total*100
    print('Acertos '+str(count)+'/'+str(apostas)+' = %.2f'%(p_final)+' %')
    count += 1