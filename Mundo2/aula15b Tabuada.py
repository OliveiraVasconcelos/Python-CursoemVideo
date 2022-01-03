print('~'*30)
print('           TABUADAS')
print('~'*30)

n = int(input('Quer ver a tabuada de qual valor?'))

while n >=0:
    for i in range(1,11):
        print(f'{n} x {i} = {n*i}')
    print('-'*30)
    n = int(input('Quer ver a tabuada de qual valor?(Digite um valor negativo para parar): '))
    print('-'*30)
print('Programa encerrado!')