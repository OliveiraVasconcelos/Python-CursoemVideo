
from random import randint
def sorteia():
    numeros=[]
    print(f'Sorteando 5 valores da lista: ',end=' ')
    for i in range(5):
        a = (randint(0,10))
        print(a,end=' ')
        numeros.append(a)
    print('PRONTO!')    
    return numeros

def somaPar(l):
    par = []
    for i in l:
        if i % 2 == 0:
            par.append(i)
    return sum(par)        


lista = sorteia()
par = somaPar(lista)
print(f'Somando os valores pares de {lista}, temos {par}')