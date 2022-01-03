lista = []
maior = 0
menor = 0
for i in range(7):
    idade = int(input(f'DIGITE A IDADE DA {i +1} PESSOA: '))
    lista.append(idade)

for idade in lista:
    if idade >= 21:
        maior += 1
    else:
        menor += 1
print('\004'*30)        
if maior > 1:        
    print(f'Das 7 idades {maior} são maiores de idade!')        
elif maior <= 1:
    print(f'Das 7 idades {maior} é maior de idade!')        

if menor > 1:
    print(f'Das 7 idades {menor} são menores de idade!')
elif menor <=1:
    print(f'Das 7 idades {menor} são menores de idade!')    
print('\004'*30)    