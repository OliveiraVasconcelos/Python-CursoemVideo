lista = []
for i in range (5):
    n = int(input('Digite um valor'))
    if i == 0 or n > lista[-1]:
        lista.append(n)
        print('Adicionado ao final da lista')
    else: 
        pos=0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos,n)
                print(f'Adicionado na posição {pos} da lista.')
                break    
            pos += 1
print('Os valores adicionados a lista em ordem são ',end='')
print(*lista,sep=',')
