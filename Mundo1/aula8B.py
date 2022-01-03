from math import hypot
adjacente = float(input('Cateto adjacente: '))
oposto = float(input('Cateto oposto: '))
print('        HIPOTENUSA!')
print('*'*30)
print(f'O cateto adjacente é {adjacente}')
print(f'O cateto oposto é {oposto}')
print(f'A hipotenusa é {hypot(adjacente,oposto):.5f}')
print('*'*30)