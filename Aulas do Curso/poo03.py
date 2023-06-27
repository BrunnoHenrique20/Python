class Pessoa:
    def __init__(self, nome:str, sexo:chr, idade:int):
        self.nome = nome
        self.sexo = sexo
        self.idade = idade

    def get_nome(self):
        return self.nome

    def get_sexo(self):
        return self.sexo

    def get_idade(self):
        return self.idade

class Amigo(Pessoa):
    def __init__(self, nome:str, sexo:chr, idade:int, diaAniversario:str):
        super().__init__ (nome, sexo, idade)
        self.diaAniversario = diaAniversario

    def get_diaAniversario(self):
        return self.diaAniversario

    def saudacao(self):
        print('')
        print(f'Nome: {self.nome}')
        print(f'Sexo: {self.sexo}')
        print(f'Idade: {self.idade} anos')
        print(f'Dia do Aniversario: {self.diaAniversario}')

amigo = Amigo('Brunno','H',26,'29/08/1996')
amigo.saudacao()