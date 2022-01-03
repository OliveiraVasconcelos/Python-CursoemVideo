lista=[]
listaPar=[]
listaImpar=[]

while True:
    n = int(input('Digite um número aí: '))
    lista.append(n)
    opcao = input('Gostaria de continuar? [S/N] ')
    while opcao not in 'SsNn':
        opcao = input('Gostaria de continuar? [S/N] ')
    if opcao in 'Nn':
        break    
for i in lista:
    if i % 2 == 0:
        listaPar.append(i)
    else:
        listaImpar.append(i)
print('-='*20)
print(f'A lista completa é: ',end='')
print(*lista,sep=', ')
print(f'A lista de pares é: ',end='')
print(*listaPar,sep=', ')
print(f'A lista de ímpares é: ',end='')
print(*listaImpar,sep=', ')
