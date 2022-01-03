print('='*20)
print('Sequência de Fibonacci')
print('='*20)
n = int(input('Quantos elementos da sequência de Fibonacci gostaria de ver? '))

anterior = 0
proxima = 1
soma = 1
cont = 0
while cont < n:
    print(f'{anterior} -> ',end='')
    soma = proxima + anterior
    anterior = proxima
    proxima = soma
    cont += 1
print('FIM!')    


"""for i in range(0,n):
    print(anterior)
    soma = proxima + anterior
    anterior = proxima
    proxima = soma
    cont += 1
    """

     