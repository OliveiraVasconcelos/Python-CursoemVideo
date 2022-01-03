n1 = int(input('Primeiro numero: '))
n2 = int(input('Segundo número: '))
n3 = int(input('Terceiro número: '))

if n1 < n2 and n1 < n3:
    print(n1,'É o menor número!')
elif n2 < n1 and n2 < n3:
    print(n2,'É o menor número')
elif n3 < n1 and n3 < n2:
    print(n3,'É o menor número!')                        

if n1 > n2 and n1 > n3:
    print('É o maior número! ')
elif n2> n1 and n2 > n3:
    print('É o maior número! ')
elif n3 > n1 and n3 > n2:
    print('É o maior número! ')        