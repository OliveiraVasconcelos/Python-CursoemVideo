a= float(input('Primeira nota: '))
b = float(input('Segunda nota: '))
media = (a + b)/2

if media < 5:   
    print(f'Tirando {a} e {b}, a média do aluno é {media:.2f}')
    print('REPROVADO!')
elif media >= 5 and media < 6.9:
    print(f'Tirando {a} e {b}, a média do aluno é {media:.2f}')
    print('RECUPERAÇÃO!')
else:
    print(f'Tirando {a} e {b}, a média do aluno é {media:.2f}')
    print('ALUNO APROVADO!')
