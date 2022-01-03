media = 0
registro = []
idadesMaior=[]
while True:
    pessoa ={} 
    pessoa['nome'] = input('Nome: ').title()
    sexo = input('Sexo: [M/F] ')
    while sexo not in ('MmFf'):
        sexo = input('ERRO! Digite apenas "M" ou "F": ')
    pessoa['sexo'] = sexo
    idade = int(input('Idade: '))
    while idade not in range(0,200):
        idade=int(input('Por favor, digite sua idade: '))
    pessoa['idade'] = idade
    media += idade    
    opcao = input('Deseja continuar? [S/N] ')
    while opcao not in 'SsNn':
        opcao=input('Digite apenas "S" ou "N". Deseja continuar? [S/N] ')
    registro.append(pessoa.copy())
    if opcao in 'Nn':
        break
media = media/len(registro)    
print('-='*25)
print('\033[1;31m      RESUMO!\033[m')
print(f'O grupo tem {len(registro)} pessoas.')
print(f'A média de idade é de {media:.2f} anos.')
print(f'As mulheres cadastradas foram: ',end='')
for i in registro:
    if i['sexo'] in 'Ff':
        print(i['nome'],end=' ')
print(f'\nLista das pessoas que estão acima da média: ')
for i in range(len(registro)):
    if registro[i]['idade'] > media:
        print(f'nome = {registro[i]["nome"]}; sexo = {registro[i]["sexo"]}; idade = {registro[i]["idade"]}')
print('\033[1;31m   << ENCERADO >>  \033[m')