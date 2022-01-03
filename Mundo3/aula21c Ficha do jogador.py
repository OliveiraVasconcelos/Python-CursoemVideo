def ficha(n=0,g=0): 
    if n == 0:
        n = '<desconhecido>'            
    print(f'O jogador {n} fez {g} gol(s) no campeonato.')
    


n = input('Nome do jogador: ').upper()
gols = input('Número de Gols: ')
if gols.isnumeric():
    gols = int(gols)
else:
    gols = 0
if n.strip() == '':
    ficha(g=gols)        
else:
    ficha(n,gols)