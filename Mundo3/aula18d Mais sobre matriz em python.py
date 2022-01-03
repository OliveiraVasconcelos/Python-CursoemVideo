lista = [[], [], []]
soma=somapar=0

for l in range(3):
    for c in range(3):
        if c == 2:
            n = int(input(f'Digite um valor para [{l}, {c}]: '))
            lista[l].append(n)
            soma += n
            if n % 2 == 0:
                somapar += n
        else:
            n = int(input(f'Digite um valor para [{l}, {c}]: '))    
            lista[l].append(n)
            if n % 2 == 0:
                somapar += n
print('-='*27)
for l in range(3):
    for c in range(3):
        print(f'[{lista[l][c]:^5}]',end='')
    print('')    
print('-='*27)
print(f'A soma dos valores pares é {somapar} ')
print(f'A soma da terceira coluna é {soma} ')
print(f'O maior valor da sagunda linha foi {max(lista[1])}')
