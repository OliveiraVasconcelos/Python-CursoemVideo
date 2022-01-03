sal = float(input('Digite o salário: '))

if sal > 1250:
    nsal = sal + (sal*0.1)
    print(f'O salário é {sal:.2f}, e o salário com acréscimo de 10% é {nsal:.2f} ')
else:
    nsal = sal + (sal*0.15)
    print(f'O salário é {sal:.2f}, e o salário com acréscimo de 15% é {nsal:.2f}')
        