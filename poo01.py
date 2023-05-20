class Carro:  # classe Carro
    # primeira definição a executar (def)
    def __init__(self, marca, cor, ano, velocidade, quant_rodas, quant_passageiros, tamanho):
        # Os Atributos são colocados junto do parenteses no init para facilitar

        # utilizamos o self para definir as características da própria classe carro
        self.marca = marca
        self.cor = cor
        self.ano = ano
        self.velocidade = velocidade
        self.quant_rodas = quant_rodas
        self.quant_passageiros = quant_passageiros
        self.tamanho = tamanho

    def andar(self):  # agora nosso carro pode andar (um método)
        print("Está andando!")

    def buzinar(self):  # self significa referir ao proprio objeto ou classe que está sendo atribuido
        print("Está buzinando!")

    def acenderLuz(self):
        print("Acendeu a Luz!")


# Criando um Objeto Tesla com os atributos ja definidos
tesla = Carro("Tesla", "Prata", 2022, 120, 4, 6, 3.5)
fusca = Carro("Fusca", "Amarelo", 2005, 80, 4, 4, 2.5)

print(' = '*10 + ' ATRIBUTOS DO TESLA'+' = '*10)

print(tesla.marca)
print(tesla.cor)  # cor do objeto tesla é igual a self.cor (vermelho)
print(tesla.ano)
print(tesla.tamanho)
print(tesla.velocidade)
print(tesla.quant_passageiros)
print(tesla.quant_rodas)

print(' = '*10 + ' MÉTODOS DO TESLA'+' = '*10)

# vai executar o que está dentro do método buzinar por isso ja executa o print
tesla.buzinar()
tesla.andar()
tesla.acenderLuz()

print(' = '*10 + ' ATRIBUTOS DO FUSCA'+' = '*10)

print(fusca.marca)
print(fusca.cor)  # cor do objeto tesla é igual a self.cor (vermelho)
print(fusca.ano)
print(fusca.tamanho)
print(fusca.velocidade)
print(fusca.quant_passageiros)
print(fusca.quant_rodas)

print(' = '*10 + ' MÉTODOS DO FUSCA'+' = '*10)

# vai executar o que está dentro do método buzinar por isso ja executa o print
fusca.buzinar()
fusca.andar()
fusca.acenderLuz()

print(f'O carro {tesla.marca} vai acender a luz')  # esse é o chamado f-string uma forma melhor e atualizada para programar