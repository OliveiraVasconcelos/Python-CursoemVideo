print('-'*30)
print('\033[33;44mBALANÇA!\033[m')
print('-'*30)
lista =[]
for i in range(5):
    peso = float(input(f'Digite o peso da {i+1} pessoa Kg: '))
    lista.append(peso)

a = max(lista)
b = min(lista)

print(f'O mairo peso lido foi {a}KG')
print(f'O menor peso lido foi {b}KG')