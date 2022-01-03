###faça um algoritmo que leia o salário de um funcionário e mostre seu novo sálario, com 15%de aumento
nome = input('Digite o nome do funcionário: ')
sal = float(input('Digite o valor do salario: '))
novo_salario = sal +(sal*0.15)
print(f'O  salário do {nome} é R$:{sal:.2f}, com 15% de acrecimo fica R$:{novo_salario:.2f}')
