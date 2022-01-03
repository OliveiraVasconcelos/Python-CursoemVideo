from random import randint
from time import sleep
from operator import itemgetter
jogadores = {'jogador 1': randint(1,6),
             'jogador 2': randint(1,6),  
             'jogador 3': randint(1,6),
             'jogador 4': randint(1,6),            
            }
ordem= sorted(jogadores.items(), key=itemgetter(1), reverse=True)

print('-='*20)            
for pos,j in jogadores.items():
    print(f'   O {pos} tirou > {j} < no dado.')
    sleep(1)
print('-='*20)
print('\033[1;33m        -=-=-=< RANKING >=-=-=-\033[m')   
for v,i in enumerate(ordem):
    print(f'\033[1;31m  O {v+1}° lugar é do {i[0]} que tirou {i[1]} no dado!')
