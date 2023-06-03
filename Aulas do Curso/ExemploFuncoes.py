# import Funcoes 
# import Funcoes as f
from Funcoes import calculaFgts
from Funcoes import calculaInss
from Funcoes import calculaHoraExtra
from Funcoes import calculoSalarioCOMEXTRA
from Funcoes import calculoSalarioSEMEXTRA

aliquotaInss = 0.075
aliquotaFgts = 0.09
cargaMensal = 220

salarioBruto = float(input('Digite o salário Bruto: '))
descontos = float(input('Digite o valor dos descontos: '))

qtdHoraExtra = 0.0
resposta = str(input('Existe hora extra? [S/N]: '))

if resposta == 'S':
    qtdHoraExtra = float(input('Digite a quantidade de horas extras trabalhadas: '))
    valorhoraextra = calculaHoraExtra(salarioBruto,cargaMensal,qtdHoraExtra)

valorInss = calculaInss(salarioBruto,aliquotaInss)
valorFgts = calculaFgts(salarioBruto,aliquotaFgts)


if resposta == 'S':
    resultado = calculoSalarioCOMEXTRA(salarioBruto,descontos,valorInss,valorFgts,valorhoraextra)
else:
    resultado = calculoSalarioSEMEXTRA(salarioBruto,descontos,valorInss,valorFgts)

print(resultado)