def tem_repeticao(lista):
    for numeral in lista:
        if lista.count(numeral) > 1:
            return True
    return False