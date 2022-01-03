def troca(lista, i, j):
    lista[i], lista[j] = lista[j], lista[i]

def empurra(s,n):
    for i in range(n-1):
        if s[i] > s[i+1]:
            troca (s,  i, i+1)

def bubble_sort2(s):
    n = len(s)
    while n > 1:
        empurra(s,n)
        n -=1
    return lista    

def bubble_sort(s):
    n = len(s)
    while n > 1:
        empurra(s,n)
        n -=1

lista = [40, 30, 20, 50,10]
nova_lista = bubble_sort2
print(lista)
bubble_sort2(lista)
