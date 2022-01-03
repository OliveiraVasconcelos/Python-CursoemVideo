lista=[[],[],[]]
for i in range(3):
    for j in range(3):
        n = int(input(f'Digite um valor para [{i},{j}]: '))
        lista[i].append(n)
for i in range(3):
    for j in range(3):
        print(f'[{lista[i][j]:^5}]',end='')
    print('')

"""for i in range(0,len(lista),3):
    print(f'[ {lista[i]} ] [ {lista[i+1]} ] [ {lista[i+2]} ]')"""