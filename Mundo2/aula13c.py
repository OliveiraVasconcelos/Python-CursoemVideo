soma = 0
impares = 0
m_3 = 0
for i in range(501):
    if i % 2 == 1:
        impares +=1
        if i % 3 == 0:
            print(i)
            m_3 += 1
            soma += i


print(f'Entre 0 500 temos {impares} números ímpares, e {m_3} deles são multiplos de 3!')
print(f'A soma dos multiplos de 3 é {soma}')        
