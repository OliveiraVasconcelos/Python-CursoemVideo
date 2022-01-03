from datetime import date
def voto(ano):
    atual = date.today().year
    idade = atual-ano
    if idade < 16:
        frase = 'VOTO NEGADO!'
    elif idade >=16 and idade < 18:
        frase = 'VOTO OPICIONAL!'    
    elif idade  >=18 and idade < 65:
        frase = 'VOTO OBRIGATÓRIO!'    
    else:
        frase = 'VOTO OPICIONAL!'    
    return frase,idade

print('-='*17)        
n = int(input('Digite o ano de nascimento: '))
print('-='*17)
frase,idade=voto(n)
print(f'Para quem tem ' f'\033[1;31m{idade}\033[m ' 'anos,' f' \033[1;34m{frase}')