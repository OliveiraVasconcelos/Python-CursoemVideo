###desenvolva um programa que leia duas notas e exiba a média de um aluno:
nome = input('Digite o nome do aluno: ')
nt1 = float(input('Digite a primeira nota: '))
nt2 = float(input('Digite a segunda nota: '))
media = (nt1 + nt2)/2
print('A primeira nota do {} foi {}, a segunda foi {} e a media é {}!'.format(nome, nt1, nt2, media))
