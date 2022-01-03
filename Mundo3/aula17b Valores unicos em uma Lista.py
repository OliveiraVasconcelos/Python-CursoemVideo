lista= []
while True:
    valor = int(input('Digite um valor: '))
    if valor not in lista:
        lista.append(valor)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor duplicado, impossível adicionar!')
    opcao = input('Deseja continuar? [S/N] ')
    while opcao not in 'SsNn':
        opcao = input('Deseja continuar? [S/N] ')
    if opcao in 'Nn':
        break
print('-='*25)
if len(lista) > 1:        
    print('Voce digitou os valores ', end='')
    print(*sorted(lista),sep=', ')
elif len(lista) == 1:
    print(f'Você digitou o valor {valor}')    
print('OBRIGADO POR PARTICIPAR!')
