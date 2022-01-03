n = int(input('\033[36mNúmero: (999 para parar)\033[36m'))
soma = n
cont = 0
while n != 999:
    n = int(input('\033[36mNúmero: (999 para parar)\033[36m'))
    soma +=n
    cont += 1
print(f'Foram digitados {cont} números')
print(f'A soma de todos eles é: {soma-999}')    