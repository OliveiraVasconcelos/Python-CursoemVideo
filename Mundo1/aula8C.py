import math
x = float(input('Digite um ângulo: '))
tangente = math.tan(math.radians(x))
cos = math.acos(math.radians(x))
seno = math.asin(math.radians(x))
print(f'O cosseno de {x} é {cos:.2f}')
print(f'O seno de {x} é {seno:.2f}')
print(f'A tangente de {x} é {tangente:.2f}') 