print('GERADOR DE PA: ')
print('-=-'*10)
termo = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))
termos = 0
cont = 1

while cont <= 10:
    print(f'{termo} -> ',end='')   
    termo += razao
    cont+=1
    termos+=1
print('PAUSA')
cont = 1

opcao = int(input('Quantos termos você quer mostrar a mais? '))
while opcao > 0:
    for i in range(opcao):
        print(f'{termo} -> ',end='')
        termo += razao
        cont += 1
        termos += 1
    print('PAUSA')
    opcao = int(input('Quantos termos você quer mostrar a mais? '))
print(f'Progressão finalizada com {termos} termos.')