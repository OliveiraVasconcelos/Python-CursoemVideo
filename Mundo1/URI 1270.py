a = int(input())
b = int(input())
m = 1

if b < a:
    print('Nenhuma tabuada no intervalo!')

for i in range(a,b + 1):
    for n in range(1,11):
        print(f'{i} x {n} = {i*n}')
    print('-'*10)   




"""for i in range(a,b+1): 
    for i in range (1,11):
        print(f'{i} x {m} = {i*m}')
    m +=1 
    print('-'*10)"""
 