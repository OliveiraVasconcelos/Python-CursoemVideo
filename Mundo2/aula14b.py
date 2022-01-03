from random import randint
tentativa =1

print('='*20)
print('JOGO DA ADIVINHAÇÂO')
print('='*20)
print('-Sou seu computador...')
print('-Pensarei em um número de 0 a 10!')
print('-Consegue adivinhar???')

pc = randint(0,10)
print(pc)
palpite=int(input('Palpite? R:'))
while palpite != pc:
    tentativa += 1
    if palpite > pc:
        palpite = int(input('Menos. Palpite? R:'))
    else:
        palpite = int(input('Mais. Palpite? R:'))
print('\033[34mACERTOU MISERÁVEL!')
print(f'Voçê só precisou de {tentativa} tentativas')