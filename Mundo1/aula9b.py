#variaveis
numero = int((input('Digite um número de 0 à 9999: ')))
digito = str(numero)
digito = len(digito)
u = numero // 1 % 10
d = numero // 10 % 10
c = numero // 100 % 10
m = numero // 1000 % 10
#calculo do programa

print(f'Digitos: {digito}')
print('Unidade: {}'.format(u))
print('Dezena: {}'.format(d))
print('Centena:{}'.format(c))
print('milhar:{}'.format(m))


### 20/05/2021  REFAZER TODA ESSA MERDA!!!!!! ###
### 21/05/2021 REFEITO !!!!!! ###