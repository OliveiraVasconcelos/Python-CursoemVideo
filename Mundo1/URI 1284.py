a = int(input())
lista = []
lista2 = []
lista3 = []
alunos = 0
novanota = 0
while a != alunos:
    n=float(input())
    lista.append(n)
    alunos += 1

for i in lista[0:]:
    n1 = float(input())
    lista2.append(n1)   
    while n1 == 10:
        if (lista[i] + 2) <= 10:
            lista3.append(lista[i]+ 2.00)
        else:
            lista3.append(10.0)
    i += 1           
    novanota += 1

print(f'NOTAS ALTERADAS: {novanota}')

print(f'original: {lista[0]:.2f} | final: {lista3[0]:.2f}')
        
