aluno = {
        }
aluno['nome'] = str(input('Nome: ').title())
aluno['média'] = float(input(f'Média de {aluno["nome"]} é: '))
print('-='*20)
if aluno['média'] >= 7:
    aluno['situação'] = 'Aprovado!'
elif aluno ['média'] < 5:
    aluno['situação'] = 'Reprovado!'   
else:
    aluno['situação']='Recuperação!'

    
print(f'O nome é igual a {aluno["nome"]}') 
print(f'Média é igual a {aluno["média"]}')
if aluno['situação'] == 'Aprovado!':
    print(f'Situação do {aluno["nome"]}:', f'\033[1;34m{aluno["situação"]}\033[m')   
elif aluno['situação'] == 'Recuperação':
    print(f'Situação do {aluno["nome"]}:', f'\033[1;33m{aluno["situação"]}\033[m')
else:
    print(f'Situação do {aluno["nome"]}:', f'\033[1;31m{aluno["situação"]}\033[m')    