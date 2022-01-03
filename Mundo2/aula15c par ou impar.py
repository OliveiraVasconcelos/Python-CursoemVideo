from random import randint
vitorias = 0
total = 0
partidas = 0
print('\033[35m=-=\033[35m'*15)
print('\033[35mJOGO DO PAR OU ÍMPAR\033[35m')
print('=-='*15)

n = int(input('Digite um número: '))
while n > 0:
    pc = randint(0,10)
    total = pc+n
    parOUimpar=input('Par ou ímpar? [P/I] ')

    while parOUimpar not in 'IiPp':
        parOUimpar=input('Par ou ímpar? [P/I]')

    if parOUimpar in 'Pp':
        if total % 2 == 0:
            print('-'*30)
            print(f'Você jogou {n} e o computador {pc}. O total de {total} é PAR!')
            print('-'*30)
            print('Você VENCEU!!!')
            print('Vamos jogar novamente...')
            vitorias+=1
        elif total % 2 != 0:
            print('-'*30)
            print(f'Você jogou {n} e o computador {pc}. O total de {total} é ÍMPAR!')
            print('-'*30)
            print('Você PERDEU!!!')
            print('Vamos jogar novamente...')
    elif parOUimpar in 'Ii':
        if total % 2 == 0:
            print('-'*30)
            print(f'Você jogou {n} e o computador {pc}. O total de {total} é PAR!')
            print('-'*30)
            print('Você PERDEU!!!')
            print('Vamos jogar novamente...')
        elif total % 2 != 0:
            print('-'*30)
            print(f'Você jogou {n} e o computador {pc}. O total de {total} é ÍMPAR!')
            print('-'*30)
            print('Voce VENCEU!!!')
            print('Vamos jogar novamente...')    
            vitorias+=1
    n = int(input('Digite um número: '))
    partidas +=1
print('\033[36mGAME OVER!\033[36m')
if vitorias>1:
    print(f'\033[36mVocê jogou {partidas} e venceu {vitorias} vezes!')
else:
    print(f'\033[36mVocê jogou {partidas} venceu {vitorias} vez!')                