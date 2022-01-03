n = int(input('Digite um número: '))
d = 0

for i in range (1,n+1):
    if n % i == 0:
        print(f'\033[34m{i}\033[m', end=' ')
        d += 1
    else:
        print(f'\033[33m{i}\033[m', end=' ') 

if d == 2:
    print()
    print(f'O número {n} foi divisível {d} vezes')
    print('E por isso ele é primo!')
else:
    print()
    print(f'O número {n} foi divisivel {d} vezes')
    print('E por isso ele não é primo!')               
    









#print(f'\033[45;36m{i}\033[m',end='')
 #       print(f'\033[36;45m{i}\033[m',end='-')