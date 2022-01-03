lista = []
a = 0
contPar=0
listaPar=[]
for i in range (4):
    a = int(input('Digite um número: '))
    lista.append(a)

tupla = (lista[0],lista[1],lista[2],lista[3])
print(f'Você digitou os valores : ',end='')
for i in range (4):
    print(f'{tupla[i]}',end=' ')
print('')

cont9=tupla.count(9)
if cont9 == 0:
    print('O valor 9 apareceu 0 vezes')
elif cont9 == 1:
    print(f'O valor 9 apareceu {cont9} vez')    
elif cont9 > 1:
    print(f'O valor 9 apareceu {cont9} vezes')

if 3 in tupla:     
    valor3=tupla.index(3)
    print(f'O valor 3 foi digitado na {valor3+1}° posição')
else:
    print('O valor 3 não foi digitado em nenhuma posição')    

for i in tupla:
    if i % 2 == 0:
        contPar+=1
        listaPar.append(i)
if contPar == 0:
    print(f'Nenhum valor par foi digitado.')
elif contPar == 1:
    print(f'Apenas um número par foi digitado, o ',end='')
    print(*listaPar)    
elif contPar > 1:
    print(f'Os valores pares digitados foram: ',end='')
    print(*listaPar)            
else: 
    print('ERRO')    