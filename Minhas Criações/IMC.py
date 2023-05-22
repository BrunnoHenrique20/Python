print('='*20+'CALCULO DO IMC'+'='*20)

peso = float(input('Digite o peso em KG: '))
altura_converter = float(input('Digite a altura em CM: '))

altura = altura_converter/100
imc = int(peso/(altura**2))

if imc < 18.5 :
    categoria = 'Baixo Peso'
elif imc < 25 :
    categoria = 'Peso Normal'
elif imc < 30 :
    categoria = 'Sobrepeso'
elif imc < 40 :
    categoria = 'Obeso'
elif imc >= 40 :
    categoria = 'Obeso Mórbido'

print('')
print('Seu IMC é de '+str(imc)+' e você está na categoria: '+categoria)
