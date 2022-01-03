print('-=-'*16)
print('        ANALISADOR DE TRIÂNGULOS')
print('-=-'*16)

r1 = float(input('Digite o comprimento da reta1: '))
r2 = float(input('Digite o comprimento da reta2: '))
r3 = float(input('Digite o comprimento da reta3: '))

if r1 + r2 > r3 and r2 + r3 > r1 and r1 + r3 > r2:
    print('É possível formar um triângulo!')
else:
    print('Não é possível formar um triângulo!')            