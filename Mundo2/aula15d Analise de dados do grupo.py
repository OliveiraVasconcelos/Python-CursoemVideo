
maiordeidade=0
homens=0
mullheresMenorde20=0
fimdoprograma = 'FIM DO PROGRAMA'
print('-'*26)
while True:
    print('   Cadastre uma pessoa')
    print('-'*26)
    idade = int(input('Idade: '))
    if idade >= 18:
        maiordeidade+=1
    sexo= input('Sexo: ')
    while sexo not in 'MmFf':
        sexo = input('Sexo: ')
    print('-'*26)
    
    if sexo in 'Ff':
        if idade <20:
            mullheresMenorde20 += 1    
    elif sexo in 'Mm':
        homens+=1

    opcao=input('Quer continuar? [S/N]')
    
    while opcao not in 'SsNn':
        opcao=input('Quer continuar? [S/N]')
    if opcao in 'Nn':
        print(f'{fimdoprograma:=^29}')
        break
        
    print('-'*26)
print(f'Total de pesssoas com mais de 18 anos: {maiordeidade}')    
print(f'Ao todo temos {homens} homens cadastrados')
print(f'E temos {mullheresMenorde20} mulheres com menos de 20 anos')
