print('\033[1;93m')
print('\004'*20)
print('\033[1;93m10 TERMOS DE UMA PA\033[1;93m')
print('\004'*20)

primeiro_termo=int(input('Primeiro termo: '))
razao = int(input('Razão: '))
lista = []

for i in range(10):
    sequencia = primeiro_termo
    lista.append(sequencia)
    primeiro_termo += razao
print(f'{lista[0]} -> {lista[1]} -> {lista[2]} -> {lista[3]} -> {lista[4]} -> {lista[5]} -> {lista[6]} -> {lista[7]} -> {lista[8]} -> {lista[9]} -> FIM')    
    
