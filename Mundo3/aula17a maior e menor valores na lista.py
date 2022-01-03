lista = []
posicao = []
menorpos = []
for i in range (5):
    lista.append(int(input(f'Digite um número para a posição {i}: ')))
for pos,i in enumerate(lista):
    if i == max(lista):
        posicao.append(pos)
    elif i == min(lista):
        menorpos.append(pos)

print('-='*30)
print('Você digitou os valores ',end='')
print(*lista)
if len(posicao)>1:
    print(f'O maior valor digitado foi o {max(lista)} digitado nas posições ',end='')
    print(*posicao,sep='...',end='...')
else:
    print(f'O maior valor digitado foi o {max(lista)} digitado na posição ',end='')    
    print(*posicao)
if len(menorpos) > 1:
    print(f'\nO menor valor digitado foi o {min(lista)} digitado nas posições ',end='') 
    print(*menorpos,sep='...',end='...')   
else:
    print(f'\nO menor valor digitado foi o {min(lista)} digitado na posição ',end='') 
    print(*menorpos,end='...')   
   