###faça um algoritmo que leia o preço de um produto e mostra seu novo preço
### com 5% de desconto

preco = float(input('\033[4;35;43mQual é o valor do produto? \033[m'))
desconto = preco*0.05
comDesconto = preco - desconto
print(f'\033[4;35;43mO valor da mercadoria é R$:{preco:.2f} e com desconto de 5% fica R$:{comDesconto:.2f}\033[m')

