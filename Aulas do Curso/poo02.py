class Televisao:
    def __init__(self, min, max):  # Classe Televisão com os atributos
        self.canal = 2  # Atributo canal ja definido inicialmente para 2
        self.ligada = False  # A TV está desligada!
        self.cmin = min
        self.cmax = max

    def muda_canal_para_baixo(self):
        # if self.canal - 1 >= self.cmin:
        if tv_sala.ligada == True:
            self.canal -= 1
        else:
            print ('TV DESLIGADA, IMPOSSIVEL MUDAR CANAL!')
    
    def muda_canal_para_cima(self):
        # if self.canal + 1 <= self.cmax:
        if tv_sala.ligada == True:
            self.canal += 1
        else:
            print ('TV DESLIGADA, IMPOSSIVEL MUDAR CANAL!')

tv_sala = Televisao(1,99)  # criar um objeto a partir de uma classe (mesma coisa que instanciar uma classe)
tv_sala.ligada = True  # A TV está ligada!

print(f'Canal Selecionado: {tv_sala.canal}')  # SHIFT + ALT + Seta para Baixo = Copia essa linha para a linha de baixo
tv_sala.muda_canal_para_cima()  # Ação de mudar o canal para próximo canal
print(f'Canal Selecionado: {tv_sala.canal}')  # Mostra o próximo canal
tv_sala.muda_canal_para_cima()
tv_sala.muda_canal_para_cima()
tv_sala.muda_canal_para_cima()
tv_sala.muda_canal_para_baixo()
tv_sala.muda_canal_para_baixo()
tv_sala.muda_canal_para_cima()
print(f'Canal Selecionado: {tv_sala.canal}')