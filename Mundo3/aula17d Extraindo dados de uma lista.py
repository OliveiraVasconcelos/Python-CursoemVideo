lista = []
while True:
    n = int(input('Digite um valor: '))
    lista.append(n)
    opcao = input('Quer continuar? [S/N]')
    while opcao not in 'SsNn':
        opcao=input('Quer continuar? [S/N]')
    if opcao in 'Nn':
        break
print(f'Fora digitados {len(lista)} elementos! ') 
print(f'a lista em ordem decrescente: ',end='')
print(sorted(lista, reverse=True))
if 5 in lista:
    print(f'O valor 5 está na lista!')   
else: 
    print('O valor 5 NÃO está na lista...')    