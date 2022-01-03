
def numeroigual(a):
    b = str(a)
    lista = []
    for i in b:
        lista.append(i)
    for j in lista:
        if lista.count(j) >1:
            return None   
        elif lista.count(j) == 1:
            casa = 1
            lista.clear
        else:
            return None    
    return casa
  
num1,num2 = input().split()
n1 = int(num1)
n2 = int(num2)
somadecasas=0
for i in range(n1,n2+1):
    a = numeroigual(i)
    if a == 1:
        somadecasas+=1

print(somadecasas)        