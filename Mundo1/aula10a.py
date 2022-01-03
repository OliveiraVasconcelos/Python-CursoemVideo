"""from random import randint
n = randint(0,5)

x = int(input('Qual número você chuta?'))
while ((x > 5) or (x < 0)):
    x=int(input('Digite novamente:'))
if x == n:            
    print('Parabéns, você acertou!')
    print('Você venceu!3')
else:
    print('OPS! Você errou!')
    print('O computador venceu!')   
print('O Correto é:',n)
print('Seu palpite foi:',x)"""     

from time import sleep
from random import randint
print('-=-'*20)
print('Vou pensar em um número de 0 a 5, tente adivinhar...')  #SEGUNDO MODO(GUANABARA) -VERSÃO JOGO
print('-=-'*20)
computador = randint(0,5)
jogador = int(input('Em qual número eu pensei?'))
print('AGUARDANDO...')
sleep(3)
if computador == jogador:
    print('PARABÉNS, você me venceu!')
else:
    print(f'GANHEI! Eu pensei no número {computador} e não no número {jogador}!')