from os import sep


lista = []
listaAux=[]
maior = menor= 0
while True:
    listaAux.append(input('Nome: '))
    listaAux.append(float(input('Peso: ')))
    if len(lista)==0:
        maior = menor = listaAux[1]
    else:
        if listaAux[1] > maior:
            maior =  listaAux[1]
        if listaAux[1] < menor:
            menor = listaAux[1]
    lista.append(listaAux[:])
    listaAux.clear()
    opcao = input('Deseja continuar? [S/N]')
    if opcao in 'Nn':
        break
print('-='*30)
print(f'Ao todo, {len(lista)} pessoas foram cadastradas ')
print(f'O maior peso registrado foi {maior}Kg. Peso de ',end='')
for p in lista:
    if p[1] == maior:
        print(f'[{p[0]}]',end=' ')
print(f'\nO menor peso registrado foi {menor}Kg. Peso de ',end='')
for p in lista:
    if p[1] == menor:
        print(f'[{p[0]}]',end=' ')
print('')
print('-='*30)