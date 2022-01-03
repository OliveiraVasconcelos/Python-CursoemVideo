from datetime import date
Anoatual = date.today().year

pessoa={}
pessoa['Nome']=str(input('Nome: ')).title()
anonascimento=int(input('Ano de nascimento: '))
idade = Anoatual-anonascimento
pessoa['idade']=idade
carteiradetrabalho=str(input('Carteirar de Trabalho (0 se não tiver): '))
if carteiradetrabalho != '0':
    pessoa['ctps'] = int(carteiradetrabalho)
    pessoa['ano de contratação']=int(input('Ano de contratação: '))
    anocontrato = pessoa['ano de contratação']
    pessoa['salário'] = float(input('Salário: '))   
    aposentedoria = (anocontrato - anonascimento) + 35  
    pessoa['aposentedoria']=aposentedoria   
print('='*30)    
for i,v in pessoa.items():
    print(f'-{i} tem o valor {v}')    
print('='*30)    