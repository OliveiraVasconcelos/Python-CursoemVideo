from random import randint
from time import sleep
print('#'*8)
print('\033[4;33mJOKENPÔ\033[m')
print('#'*8)
item = ['PEDRA','PAPEL','TESOURA']
pc = randint(0,2)

print('[0] PEDRA\n[1] PAPEL\n[2] TESOURA')
opcao = int(input('QUAL É A SUA JOGADA? '))
while opcao != 0 and opcao != 1 and opcao !=2 :
    opcao = int(input('QUAL É A SUA JOGADA? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!')
sleep(0.5)
print('-=-'*9)
print(f'O computador escolheu {item[pc]}')
print(f'Voçê jogou {item[opcao]}')
print('-=-'*9)

if pc == 0:
    if opcao == 0:
        print('EMPATE!')
    elif opcao == 1:
        print('VOÇÊ GANHOU!')
    elif opcao == 2:
        print('O COMPUTADOR GANHOU!')
    else:
         print('JOGADA INVÁLIDA!')         
elif pc == 1:
    if opcao == 0:
        print('O COMPUTADOR GANHOU!')
    elif opcao == 1:
        print('EMPATE!')
    elif opcao == 2:
        print('VOCÊ VENCEU!')
    else:
        print('JOGADA INVÁLIDA!')
elif pc == 2:
    if opcao == 0:
        print('VOCÊ VENCEU!')
    elif opcao == 1:
        print('VOCÊ PERDEU!')
    elif opcao == 2:
        print('EMPATE!')