def contagem(n):
    n=str(n)
    x = len(n)
    x = 30-x
    return x


produtos = ('Camiseta',79.90,'Camisa',100.00,'Bermuda',55.50,
'Calca Jeans',90.00,'Moletom',110.00,'Jaqueta',150.00,'Meias(par)',15.00)
nomeproduto= [] 
for i in range(0,len(produtos),2):
    nomeproduto.append(produtos[i])

print('\033[34m-\033[34m'*40)
print('                 LOJÃO')




print('-'*40)
print(f'{"TABELA DE PREÇOS":^40}')
for i in range(0,14,2):  
    print('-'*40)
    #print(f'{produtos[i]:.<30}',end=f'R$: {produtos[i+1]:.2f}')
    print(f'{produtos[i]:<30}', end='')
    print(f'{produtos[i+1]:>.2f}')

print('-'*40)    
    
    #print(f'R${produtos[i+1]:>.2f}')

