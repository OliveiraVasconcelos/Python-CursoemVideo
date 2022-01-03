from datetime import date
n = int(input('Em que ano voçê nasceu, jovem?'))
print('********************\nDATA DE NASCIMENTO =',n,'\n********************')
atual = date.today().year
idade = atual - n
n2 = idade - 18
if idade < 18:
    saldo = 18 - idade
    if saldo <=1:
        print(f'Quem nasceu em {n} tem {idade} anos em {atual}.')
        print(f'ainda faltam {saldo} anos para o alistamento.')
        print(f'Seu alistamento será em {n+18}')
    else: 
        print(f'Quem nasceu em {n} tem {idade} anos em {atual}.')   
        print(f'Ainda faltam {saldo} anos para o alistamento.')
        print(f'Seu alistamento será em {n+18}')
elif idade > 18:
    
    print(f'Quem nasceu em {n} tem {idade} anos em {atual}')
    print(f'Voçê já deveira ter se alistado há: {idade-18} anos')
    print(f'Seu alistamento foi em: {n+18}.')
else:
    print(f'Quem nasceu em {n} tem {idade} em {atual}.')
    print('Você tem que se alistar IMEDIATAMENTE!')
