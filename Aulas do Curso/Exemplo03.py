class Animal:
    def __init__(self,nome):
        self.nome = nome
    
    def falar(self):
        pass
    
class Gato(Animal):
    def falar(self):
        return 'Miau!'
    
class Cachorro(Animal):
    def falar(self):
        return 'Au Au!'
    
animais = [Gato('Missy'),Cachorro('Lassie'),Gato('Bichano')]

for animal in animais:
    print(animal.nome + ': ' + animal.falar())