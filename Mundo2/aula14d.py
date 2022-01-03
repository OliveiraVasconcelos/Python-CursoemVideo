num =int(input('Fatorial de: '))

valor = 1
cont = num 
valor=1                  #Código com -while-
while cont > 0:
    print(f'{cont}',end=' ')
    print(' x ' if cont>1 else '=',end=' ')
    valor = valor * cont 
    cont -=1
print('FIM')
print(f'O fatorial de {num}! é:', valor)    

"""num = int(input('Fatorial de: '))
valor = 1
for i in range(1,num+1):
    valor2 = valor
    valor = i * valor                       #Código com -for in range-
    print(f'{i} x {valor2} = {valor}')

print(f'O fatorial de {num}! é:',valor)    """