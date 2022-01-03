valordacasa = float(input('Informe o valor da casa R$:'))
salario = float(input('Informe o salário R$: '))
anos = int(input('Em quantas anos pretende pagar?'))

prestaçao = valordacasa / (anos*12)
limite = salario  * 0.30

if prestaçao > limite:
    print(f'Para pagar uma casa de R$:{valordacasa} em {anos} a prestação será de R$:{prestaçao:.2f}')
    print('Empréstimo negado. Sinto muito!')
else:
    print(f'Para pagar uma casa de R$:{valordacasa} em {anos} a prestação será R$:{prestaçao:.2f}')
    print('Empréstimo concedido. Parabéns!')    
print(prestaçao)
print(limite)