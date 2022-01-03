print('='*35)
cont = 1
soma = 0
n = int(input('Digite um número: '))
soma+=n
maior = n
menor = n
opcao = input('Gostaria de digitar outro número? [S/N]')
while opcao not in 'SsNn':
    opcao = input('Gostaria de digitar outro número? [S/N]')

while opcao not in 'Nn':  
        n1 = int(input('Número: '))
        if n1 > maior:
            maior = n1
            soma+=n1
            cont+=1
            opcao = input('Gostaria de digitar outro número? [S/N]')                    
        elif n1 < menor:
            menor = n1    
            soma+=n1
            cont+=1
            opcao = input('Gostaria de digitar outro número? [S/N]')  
        else:
            opcao = input('Gostaria de digitar outro número? [S/N]')  
media = soma/cont
print('\033[34m=\033[34m'*35)
print(f'\033[36mAo todo, foram digitados {cont} números\033[36m')   
print(f'\033[35mE a média entre ele é: {media}\033[35m')
print(f'\033[33mO maior número digitado foi: {maior}\033[33m')
print(f'\033[34mO menor número é: {menor}\033[34m')

print('\033[36m=\033[36m'*35)        