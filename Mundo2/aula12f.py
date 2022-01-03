from datetime import date

ano = int(input('Ano de nascimento do atleta: '))
idade = date.today().year - ano

if idade <= 9:
    print(f'O atleta com {idade} anos, compete na categoria MIRIM')
elif idade > 9 and idade <= 14:
    print(f'O atleta com {idade} anos, compete na categora INFANTIL') 
elif idade > 14 and idade <= 19:
    print(f'O atleta com {idade} anos, compete na categoria JUNIOR')
elif idade > 19 and idade <= 25:
    print(f'O atleta com {idade} anos, compete na categoria SÊNIOR')
else:
    print(f'O aluno com {idade} anos, compete na categoria MASTER')               