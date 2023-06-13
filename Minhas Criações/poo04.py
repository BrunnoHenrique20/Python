class Pessoa:
    def __init__(self, nome):
        self.nome = nome
    
    def saudacao(self):
        print(f"Olá, meu nome é {self.nome}.")


class Estudante(Pessoa):
    def __init__(self, nome, matricula):
        super().__init__(nome)
        self.matricula = matricula
    
    def saudacao(self):
        super().saudacao()
        print(f"Sou um estudante com matrícula {self.matricula}.")


estudante = Estudante("Brunno", "38172")
estudante.saudacao()
print('')
pessoa = Pessoa("Carlos")
pessoa.saudacao()