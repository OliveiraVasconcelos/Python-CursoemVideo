times =('Fortaleza','Athletico-PR','Flamengo','Atlético-GO','Atlético-MG','Bragantino','Fluminense',
'Bahia','Palmeiras','Corinthians','Ceará','Santos','Internacional','Juventude','Cuiabá',
'Sport','São Paulo','Chapecoense','Grêmio','América')
print('-'*20)
print('Os cinco primeiros colocados são: ')
for i in range(0,5):
    print(f'{i+1}° - {times[i]}')
print('-'*20)
print('~~'*20)    
print(f'Os últimos colocados são: ')
for i in range(16,20):
    print(f'{i}° - {times[i]}')
print('~~'*20)
print('='*24)    
print(f'A lista de times em ordem alfabética é: ')
print(*sorted(times),sep=', ')    
print('~~'*24)
print('#'*24)
print('A posição da Chapecoense na tabela é: ',end='')
print(times.index('Chapecoense'),end='°lugar')
print('')
print('#'*24)