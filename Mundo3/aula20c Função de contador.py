from time import sleep
from warnings import simplefilter
def contador(i,f,p):
    print(f'Contagem de {i} até {f} de {p} em {p}')
    sleep(1.5)
    if p < 0:
        p *= -1
    if p == 0:
        p = 1    
    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont}',end=' ',flush=True)
            sleep(0.5)
            cont+=p
        print('FIM!')  
    else:
        cont = i
        while cont >= f:
            print(f'{cont}',end=' ',flush=True)
            sleep(0.5)
            cont -= p
        print('FIM!')          

print('-='*14)
contador(1,10,1)
print('-='*14)
contador(10,0,2)
print('-='*14)
print('Agora é sua vez de personalizar a contagem!')
ini = int(input('Início: '))
fim = int(input('FIM: '))
passo = int(input('Passo: '))
contador(ini,fim,passo)
print('-='*14)