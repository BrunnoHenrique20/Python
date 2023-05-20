listaUm = ['João','Maria','Brunno']
listaDois = [11,12,13]
listaTres = ['EFG',2023,False,3.14]

print(listaUm)
print('_'*100)

for item in listaUm:
    print(f'Item da lista: {item}')

print('_'*100)

for numeroaserLido in listaDois:
    print(numeroaserLido)

print('_'*100)

contador = 0
for itemaserLido in listaTres:
    print(itemaserLido)
    contador = contador + 1

print('')
print('Foram Lidos ' +str(contador)+ ' itens na lista três!')
