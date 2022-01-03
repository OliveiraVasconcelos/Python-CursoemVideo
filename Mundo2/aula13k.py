soma = 0
media = 0
homem_maisvelho = 0
nome_maisvelho = ''
mulher20 = 0
print('\033[1;36m   HORA DE DIGITAR!\033[m')
for i in range(4):
    print(f'\033[35m----- {i+1}° PESSOA -----\033[m')
    nome = input('\033[34mDigite o nome: \033[34m')
    idade = int(input('\033[33mDigite a idade: \033[m'))
    soma += idade
    sexo =input('\033[38mDigite o sexo[M/F]: \033[m')
    if i == 1 and sexo in 'Mm':
        homem_maisvelho = idade
        nome_maisvelho = nome
    if sexo in 'Mm' and idade > homem_maisvelho:
        homem_maisvelho = idade
        nome_maisvelho = nome    
    if sexo in 'Ff' and idade > 20:
        mulher20 += 1

media = soma / 4
print(f'A media de idade das 4 pessoas é {media}')
print(f'O homem mais velho tem {homem_maisvelho} anos e seu nome é {nome_maisvelho}')
if mulher20 == 1:
    print(f'{mulher20} mulher tem mais de 20 anos')
else:   
    print(f'{mulher20} mulheres tem mais de 20 anos')

