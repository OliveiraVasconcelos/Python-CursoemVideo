import random
n1 = input('Nome do 1°aluno: ')
n2 = input('Nome do 2°aluno: ')
n3 = input('Nome do 3°aluno: ')
n4 = input('Nome do 4°aluno: ')
nomes = [n1, n2, n3, n4,]
random.shuffle(nomes)

print('-----ORDEM DO SORTEIO-----')
print('O sorteio chegou ao fim!')
print('A ordem para apresentar o trabalho é:')
print(nomes)
print('-'*27)
