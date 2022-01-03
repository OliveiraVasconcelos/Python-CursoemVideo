nome=input('Nome: ')
partidas=int(input(f'Quantas partidas {nome} jogou? '))
lista=[]*partidas
for i in range (partidas):
    gols=int(input(f'  Quantos gols na partida {i}?'))
    lista.insert(i,gols)
jogador={'nome': nome,
         'gols': lista,
         'total': sum(lista)
        }
print('-='*27)
print(jogador)        
print('-='*27)
for pos,v in jogador.items():
    print(f'O campo {pos} tem o valor {v}.')
print('-='*27)    
print(f'O jogador {jogador["nome"]} jogou {partidas} partidas')
for p,g in enumerate(lista):
    print(f'\033[1;3{i}m    =>\033[m',f'Na partida {p}, {nome} fez {g} gols.')
print(f'\033[1;31mFoi um total de {jogador["total"]} gols.')    