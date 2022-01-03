lista = [[],[]]

for i in range(1,8):
    n = int(input(f'Digite o {i}°. valor: '))
    if n %2 == 0:
        lista[0].append(n)
    else:
        lista[1].append(n)

print(f'Os valores pares digitados foram: ',end='')
print(*sorted(lista[0]))     
print(f'Os valores ímpares digitados foram: ',end='') 
print(*sorted(lista[1]))          