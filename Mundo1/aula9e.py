#frase = input('Digite uma frase:')
#frase1 = frase.replace('a','A')
#frase1 = frase1.count('A')
#print(f'A letra A aparece {frase1} vezes')
#frase1 = frase.find('A')
#frase = frase.find('a'[0:])
#print(f'A primeira letra A apareceu na posição {frase1+1} ')
#print(f'A ultima letra A apareceu na posição {frase}')
#print(f'A primeira letra A apareceu na posição {frase1}')
#frase1 = frase.rfind('a')
#print(f'A ultima letra A aparece na posiçao {frase1+1}')

frase = str(input('Digite uma frase: ')).replace('a','A').strip()
frase1 = frase.count('A')
print(f'A letra A aparece {frase1} vezes')
frase1 = frase.find('A')
print(f'A letra A apareceu a primeira vez na posiçao {frase1+1}')
frase1= frase.rfind('A')
print(f'A letra A apareceu a ultima vez na posição{frase1+1}')
