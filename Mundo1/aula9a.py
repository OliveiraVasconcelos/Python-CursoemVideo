nome = str(input('Digite o seu nome completo: ')).strip()
nome1=nome
print (nome)
print(f'Seu nome em maiusculo é: {(nome.upper())}')
print(f'Seu nome em minusculo é: {nome.lower()}')
nome = nome.replace(' ', '')
print(f'Seu nome tem {len(nome)} letras')
nome = nome1.split()
print(f'Seu primeiro nome tem {len(nome[0])} letras ')
