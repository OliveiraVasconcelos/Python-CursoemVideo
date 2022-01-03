a = int(input('Primeiro segmetno: '))
b = int(input('Segundo segmento: '))
c = int(input('Terceiro segmento: '))

if a == b and a == c:
    print('Os segmentos acima podem formar um triangulo EQUILÁTERO!')
elif (a == b and a != c) or (a != b and a == c):
    print('Os segmentos acima podem formar um triângulo ISÓSCELES!')
elif a != b and b != c and a != c :
    print('Os segmentos acima podem formar um triângulo ESCALENO!')        
else:
    print('Não é possível formar um triângulo')   