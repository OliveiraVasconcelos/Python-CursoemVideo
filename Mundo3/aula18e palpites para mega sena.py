from random import randint
from time import sleep
print('-='*21)
print('{:^40}'.format('MEGA SENA'))
print('-='*21)
lista=[]
n = int(input(' Quantos jogos você quer sortear? '))
print(f'-=-=-=-=-= Sorteando os {n} jogos -=-=-=-=-=')
for i in range(1,n+1):
    sleep(1.1)    
    for j in range(6):
        pc = randint(1,61)
        while pc in lista:
            pc = randint(1,61)
        lista.append(pc)
    print(f' >>>> Jogo {i}: ',end='')
    print(sorted(lista),sep=', ')
    lista.clear()
print('-='*21)
print('-=-=-=-=-=-=-=< BOA SORTE! >-=-=-=-=-=-=-=')    
print('-='*21)