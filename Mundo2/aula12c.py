a = int(input('\033[1;33;46mDigite o primeiro valor: \033[m'))
b = int(input('\033[1;33;46mDigite o segundo valor: \033[m'))

print('----------\nCOMPARAÇÃO\n---------')

if a > b:
    print(f'O primeiro número ({a}) é maior que o segundo número ({b})!')
elif a == b:
    print(f'Nem o primeiro nem o segundo\nOs números {a} e {b} são IGUAIS!')
else:
    print(f'O segundo número ({b}) é maior que o primeiro número ({a})')        