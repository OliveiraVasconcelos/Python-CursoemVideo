
n = int(input())
soma = 0
lista = []
lista.append(n)

while n >=0:
    n = int(input())
    if n >= 0:
        lista.append(n)

for i in lista:
    soma += i

media = soma/len(lista)
print(f'MEDIA: {media:.2f}')

for x in lista[0:]:
    if x < media:
        print(x)

