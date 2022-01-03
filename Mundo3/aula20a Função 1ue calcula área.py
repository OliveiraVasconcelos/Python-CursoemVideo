def area(l,c):
    area= l*c
    print(f'A área de um terreno {l}x{c} é de {area}m².')


print('\033[1;31m   Controle de Terrenos\033[m')
print('-'*26)
largura = float(input('LARGURA (m): '))    
comprimento= float(input('COMPRIMENTO (m): '))
area(largura,comprimento)