def calculoSalarioSEMEXTRA(salarioBruto,descontos,inss,fgts):
    return salarioBruto - descontos - inss - fgts

def calculoSalarioCOMEXTRA(salarioBruto,descontos,inss,fgts,qtdHoraExtra):
    return (salarioBruto - descontos - inss - fgts) + qtdHoraExtra

def calculaInss(salarioBruto,inss):
    return salarioBruto * inss

def calculaFgts(salarioBruto,fgts):
    return salarioBruto * fgts

def calculaHoraExtra(salarioBruto,cargaMensal,horasTrabalhadas):
    return (salarioBruto/cargaMensal) * horasTrabalhadas