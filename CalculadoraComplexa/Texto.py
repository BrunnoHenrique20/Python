from time import sleep

def descreve_menu():
    print('='*40+' CALCULADORA CIENTÍFICA '+'='*40)        
    print('A => Soma [+]')                                 
    print('B => Subtração [-]')                            
    print('C => Multiplicação [*]')                        
    print('D => Divisão [/]')                              
    print('E => Quadrado [x²]')                            
    print('F => Potenciação [x³]')                         
    print('G => Raiz Quadrada [sqrt]')                     
    print('H => Porcentagem [%]')                          
    print('I => Fatorial [x!]')                            
    print('J => Logaritmo [log(x)]')                       
    print('K => Equação de Segundo Grau [#]')
    print('L => Calcular uma Média (=)')              
    print('M => Conversor de Moedas ($)')                   
    print('N => Conversor de Temperatura (°C)')             
    print('O => Conversor de Tempo (¹²³)')                  
    print('P => Conversor de Medidas (<-->)')               

    print ('Q => Calculos Geométricos (§) ---EM CONSTRUÇÃO---')                 # CRIAR UM NOVO ARQUIVO .PY
    print('-'*40)
    pass

def descreve_moedas():
    print('='*40+' CONVERSOR DE MOEDAS '+'='*40)
    print('Esse conversor utiliza valores manuais:')
    # print('A) 1 REAL => 1,00')
    # print('B) 1 DOLAR => 5,00')
    # print('C) 1 EURO => 5,33')
    # print('D) 1 LIBRA => 6,22')
    # print('E) 1 PESO ARGENTINO => 0,02')
    # print('F) 1 IENE JAPONÊS 0,035 => ')
    # print('G) 1 BOLIVAR VENEZUELANO => 1/573.128,00')
    print('A) REAL => DOLAR')
    print('B) REAL => EURO')
    print('C) REAL => LIBRA')
    print('D) REAL => PESO ARGENTINO')
    print('E) REAL => IENE JAPONÊS')
    print('F) REAL => BOLIVAR VENEZUELANO')   
    print('G) DOLAR => REAL')
    print('H) EURO => REAL')
    print('I) LIBRA => REAL')
    print('J) PESO ARGENTINO => REAL')
    print('K) IENE JAPONÊS => REAL')
    print('L) BOLIVAR VENEZUELANO => REAL')
    print('')
    pass

def descreve_clima():
    print('='*40+' CONVERSOR DE TEMPERATURA '+'='*40)
    print('A) ºC => ºF')
    print('B) ºC => K')
    print('C) ºF => ºC')
    print('D) ºF => K')
    print('E) K => ºC')
    print('F) K => ºF')
    print('')
    pass

def descreve_time(pagina:str):
    if pagina==1:
        print('='*40+' CONVERSOR DE TEMPO '+'='*40)  # SEGUNDOS / MINUTOS / HORAS / DIAS / MESES / ANOS
        print('Selecione o Tipo de Valor de Entrada:')
        print('A) Segundos => Minutos | F) Minutos => Segundos')
        print('B) Segundos => Horas   | G) Minutos => Horas')
        print('C) Segundos => Dias    | H) Minutos => Dias')
        print('D) Segundos => Meses   | I) Minutos => Meses')
        print('E) Segundos => Anos    | J) Minutos => Anos')
        print('')
        print('K) >> Próxima Página >>')
        print('')

    if pagina==2:
        print('='*40+' CONVERSOR DE TEMPO '+'='*40)  # SEGUNDOS / MINUTOS / HORAS / DIAS / MESES / ANOS
        print('Selecione o Tipo de Valor de Entrada:')
        print('A) Horas => Segundos | F) Dias => Segundos')
        print('B) Horas => Minutos  | G) Dias => Minutos')
        print('C) Horas => Dias     | H) Dias => Horas')
        print('D) Horas => Meses    | I) Dias => Meses')
        print('E) Horas => Anos     | J) Dias => Anos')
        print('')
        print('K) >> Próxima Página >>')
        print('L) << Voltar Página <<')
        print('')

    if pagina==3:
        print('='*40+' CONVERSOR DE TEMPO '+'='*40)  # SEGUNDOS / MINUTOS / HORAS / DIAS / MESES / ANOS
        print('Selecione o Tipo de Valor de Entrada:')
        print('A) Meses => Segundos | F) Anos => Segundos')
        print('B) Meses => Minutos  | G) Anos => Minutos')
        print('C) Meses => Horas    | H) Anos => Horas')
        print('D) Meses => Dias     | I) Anos => Dias')
        print('E) Meses => Anos     | J) Anos => Meses')
        print('')
        print('K) << Voltar Página <<')
        print('')

def descreve_medidas(pagina:str):
    if pagina==1:
        print('='*40+' CONVERSOR DE MEDIDAS '+'='*40)
        print('A) MM => CM')
        print('B) MM => M')
        print('C) MM => KM')
        print('D) CM => MM')
        print('E) CM => M')
        print('F) CM => KM')
        print('')
        print('G) >> Próxima Página >>')
        print('')

    elif pagina==2:
        print('='*40+' CONVERSOR DE MEDIDAS '+'='*40)
        print('A) M => CM')
        print('B) M => KM')
        print('C) M => Volta ao Mundo')
        print('D) KM => M')
        print('E) KM => Volta ao Mundo')
        print('F) Ano-Luz => KM')
        print('')
        print('G) >> Próxima Página >>')
        print('H) << Voltar Página <<')
        print('')

    elif pagina==3:
        print('='*40+' CONVERSOR DE MEDIDAS '+'='*40)
        print('A) Volta ao Mundo => M')
        print('B) Volta ao Mundo => KM')
        print('C) Volta ao Mundo => Segundo-Luz')
        print('D) Segundo-Luz => KM')
        print('E) Segundo-Luz => Volta ao Mundo')
        print('F) Ano-Luz => Universo Observável')
        print('')
        print('G) << Voltar Página <<')
        print('')