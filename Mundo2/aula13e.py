soma = 0
pares = 0
for i in range(6):
    numeros = int(input('Digite um número: '))
    if numeros % 2 == 0:
        pares +=1
        soma += numeros
print(f'A soma dos {pares} números pares entre os números digitados é {soma}')

