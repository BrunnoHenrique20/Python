from time import sleep

def contar(i):
    print('Iniciando contagem...')
    u=0
    sleep(2)

    while u<99:
        u+=1
        print(f'{u} %')
        sleep(i)
    
    while u>=99 and u<99.99:
        u+=0.01
        print("{:.2f}".format(u)+' %')
        sleep(i)
    
    while u>=99.99 and u<99.9999:
        u+=0.0001
        print("{:.4f}".format(u)+' %')
        sleep(i)

    while u>=99.9999 and u<99.999999:
        u+=0.000001
        print("{:.6f}".format(u)+' %')
        sleep(i)

    while u>=99.999999 and u<99.99999999:
        u+=0.00000001
        print("{:.8f}".format(u)+' %')
        sleep(i)

    while u>=99.99999999 and u<99.9999999999:
        u+=0.0000000001
        print("{:.10f}".format(u)+' %')
        sleep(i)

print('='*50+' EXPANSÃO DO ESPAÇO-TEMPO '+'='*50)
print('')
i=float(input('Informe a velocidade de contagem: '))
contar(i)