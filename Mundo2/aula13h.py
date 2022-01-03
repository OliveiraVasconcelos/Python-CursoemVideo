from time import sleep
print('='*20)
print('PALÍNDROMO?')
print('='*20) 

frase = input('Digite sua frase: ')

lista = []
for letra in frase:
    lista.append(letra)
    if letra == ' ':
        lista.remove(' ')
a = len(lista) -1
lista2 = []        
while a >= 0:
    lista2.append(lista[a])
    a -= 1

    
print(lista, sep='-')
print(lista2, sep='-' )  
print('FAZENDO COMPARAÇÃO')
print('...')
sleep(1)
print('...')
sleep(1)
print('...')
sleep(0.5)
if lista == lista2:
    print('\004'*23)
    print('\004POLÍNDROMO DETECTADO!\004')
    sleep(1)
    print('\004SIM, É UM POLÍNDROMO!\004')
    print('\004'*23)
else:
    inverso = lista2
    print('\004'*23)
    print('\004BUSCANDO POLÍNDROMO\004')
    sleep(1)
    print(f'\004O inverso é\004',*inverso)
    print('\004NÃO É UM POLÍNDROMO!\004')
    print('\004'*23)
#if lista == polindromo:

