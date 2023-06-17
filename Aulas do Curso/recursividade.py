class ClasseMae():
    def __init__(self) -> None:
        pass
    
    def alertamae(self):
        print('Alerta!')

class FilhaClasseMae(ClasseMae):
    def __init__(self, nome, idade) -> None:
        super().__init__()
        nome = nome
        idade = idade         
        
    def __init__(self, nome, idade):
        nome = nome
        idade = idade

a = FilhaClasseMae('Marcos',18)
b = FilhaClasseMae('Brunno',26)   # as variaveis a e b se tornam do tipo "Objeto"
a.alertamae()
b.alertamae()



#def soma_lista(lista):
#    if len(lista) == 1:
#        return lista[0]
#    else:
#        return lista[0] + soma_lista(lista[1:])
#    
#lista = [1,2,3]
#print(str(soma_lista(lista)))