def menu():   
    print('='*20)
    print(('\004'*7),'MENU',('\004'*7))
    print('='*20)
    print('[1]SOMAR')
    print('[2]MULTIPLICAR')
    print('[3]MAIOR')
    print('[4]NOVOS NÚMEROS')
    print('[5]SAIR DO PROGRAMA')
    opcao = int(input('DIGITE A OPÇÃO: '))
    while opcao < 1 and opcao > 5:
        opcao = int(input('DIGITE SUA OPÇÃO: '))
    return opcao
um = int(input('Digite o primeiro número: '))
dois = int(input('Digite o segundo número: '))    
a = menu()
while a != 5:
    if a == 1:
        print(um + dois)
        continuar = input('DESEJA REALIZAR OUTRA OPERAÇÃO? [S/N]')
        if continuar in 'SsNn':
            um = int(input('Digite o primeiro número: '))
            dois = int(input('Digite o segundo número: '))
            a=menu()
        else:
             print('Volte sempre!')    
    elif a == 2:
        print(f'{um} x {dois} = {um * dois}')
        continuar = input('DESEJA REALIZAR OUTRA OPERAÇÃO? [S/N]')
        if continuar in 'SsNn':
            if continuar == 's' or 'S': 
                um = int(input('Digite o primeiro número: '))
                dois = int(input('Digite o segundo número: '))
                a=menu()
            else :
                print('Volte sempre!')        
    elif a == 3:
        if um>dois:
            print(f'O maior entre{um} e {dois} é {um}')
            continuar = input('DESEJA REALIZAR OUTRA OPERAÇÃO? [S/N]')
            if continuar in 'SsNn':
                um = int(input('Digite o primeiro número: '))
                dois = int(input('Digite o segundo número: '))
                a=menu()
        else:
            print(f'O maior entre {um} e {dois} é {dois}')
            continuar = input('DESEJA REALIZAR OUTRA OPERAÇÃO? [S/N]')
            if continuar in 'SsNn':
                if continuar == 's' or 'S':
                    um = int(input('Digite o primeiro número: '))
                    dois = int(input('Digite o segundo número: '))
                    a=menu()
                else:
                    print('Volte sempre!')
                    break    
    elif a == 4:
        print('\033[34mDigite novos números\033[m')
        um = int(input('Digite o primeiro número: '))
        dois = int(input('Digite o segundo número: '))        
        a=menu()
        
    else:
        print('Volte sempre!')
        break
