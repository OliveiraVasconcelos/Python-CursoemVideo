###faça um programa que leia a largura e a altura de uma parede em metros, calceule a sua area
### e a quantidade de tinta necessaria para pinta-la, sabendo q cada litro de tinta pinta uma area de 2m²
###para calcular a area de uma parede, basta multiplicar a LARGURA pela altura da parede

largura = float(input('Digite a largura da parede(m)'))
altura = float(input('Digite a altura da parede(m)'))
area_da_parede = largura*altura
print(f'\033[4;35;47mA area da parede é {area_da_parede:.2f}\033[m')
tinta = 2
tinta_necessaria = area_da_parede/tinta
print(f'\033[1;35;47mSerá necessario {tinta_necessaria:.2f} litros de tinta\033[m')

###utilizando a f' para formatar e ':.2f' para adicionar apenas dois pontos decimais a variavel

