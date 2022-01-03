jogadores = []

#recebendo os dados
while True:
    nome = input('Nome: ').title()
    qtdpartidas = int(input(f'Quantas partidas o {nome} jogou? '))
    lista = []*qtdpartidas
    for i in range(qtdpartidas):
        gols = int(input(f'Quantos gols na partida {i+1}? '))
        lista.insert(i,gols)
        jogador ={'nome':nome,
                  'partidas':qtdpartidas,
                  'gols':lista, 
                  'total': sum(lista)}
    jogadores.append(jogador)          
    opcao = input('Quer continuar? [S/N]: ')
    while opcao not in 'SsNn':
        opcao= input('Quer continuas? [S/N]: ')          
    if opcao in 'Nn':
        break    

#montando a estrutura da tabela com os dados!
print('-='*23)
print('cod  nome           gols           total')
print('-'*45)
for i in range(len(jogadores)):
    print(f'{i:^4}'f'\033[1;34m  {jogadores[i]["nome"]:<14}\033[m'f'  {str(jogadores[i]["gols"]):<15}',end='')
    print(f'{jogadores[i]["total"]}')    
print('-'*45)

#recebendo resposta sobre iteração do programa
while True:
    opcao = int(input('Mostra dados de qual jogador? (-1 para encerrar) '))
    
    for i in range(len(jogadores)):
        if i == opcao:
            print(f'-- LEVANTAMENTO DO JOGADOR {jogadores[i]["nome"]} --')   
            for j in range(jogadores[i]['partidas']):
                    print(f"Na jogo {j+1} o " f"\033[1;31m{jogadores[i]['nome']}\033[m"  " fez " f"{jogadores[i]['gols'][j]} gols")
    if opcao > len(jogadores)-1:
        print(f'Erro. Não existe jogador com código {opcao}, tente novamente!')
        print('-'*45)
        print('\n')
    if opcao == -1:
        print('\033[1;31m <<< ENCERRADO >>>\033[m')
        break

    
   