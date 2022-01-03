from random import randint
lista = []
for i in range(5):
    pc = randint(0,10)
    lista.append(pc)

a = (lista[0],lista[1],lista[2],lista[3],lista[4])
print(f'Os valores sorteados foram:',end=' ') 
for i in (a):
    print(f'{i}',end=' ')

print(f'\nO maior valor sorteado foi o {max(a)}')
print(f'O menor valor sorteado foi o {min(a)}')