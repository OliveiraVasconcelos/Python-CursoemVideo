"""print('-'*25)
print('\033[33mSUPER LOJÃO!\033[33m')
print('-'*25)

soma = 0
maisdemil=0
nome_mais_barato=0
mais_barato=0
lista =[]

while True:
    nomeProduto = input('Nome do produto: ')
    precoProduto= int(input('Preço : R$'))
    primeiro = precoProduto
    soma += precoProduto

    if precoProduto > 1000:
        maisdemil += 1

    if precoProduto < mais_barato:
        mais_barato = precoProduto
        nome_mais_barato = nomeProduto

    opcao = input('Deseja continuar? [S/N]')
    while opcao not in 'SsNn':
        opcao = input('Deseja continuar? [S/N]')
    if opcao in 'Nn':
        break
print(f'O total da compra foi R$:{soma:.2f} ') 
print(f'Temos {maisdemil} produtos mais de R$:1000.00')   
print(f'mais barato {mais_barato}')"""


print('-'*25)
print('\033[33mSUPER LOJÃO!\033[33m')
print('-'*25)
soma = 0
maisdemil=0

nomeProdutoMaisbarato=input('Nome do produto: ')
primeiroProduto = int(input('Preço: RS'))
soma += primeiroProduto
opcao = input('Deseja continuar? ')
while opcao not in 'SsNn':
    opcao = input('Deseja continuar? ')
if opcao in 'Nn':
    print(f'O {nomeProdutoMaisbarato} custa RS:{primeiroProduto}')    


while opcao not in 'Nn':
    nomeProduto = input('Nome do produto: ')
    precoProduto= int(input('Preço : R$'))
    soma += precoProduto
    
    if precoProduto <= primeiroProduto:
        primeiroProduto = precoProduto
        nomeProdutoMaisbarato = nomeProduto
    
    if precoProduto > 1000:
            maisdemil += 1

    opcao = input('Deseja continuar? ')
    if opcao in 'Nn':
        break

print(f'O total da compra foi R$:{soma:.2f} ') 
print(f'Temos {maisdemil} produtos mais de R$:1000.00')   
print(f'O produto mais barato é o  {nomeProdutoMaisbarato} e ele custa {primeiroProduto}')    