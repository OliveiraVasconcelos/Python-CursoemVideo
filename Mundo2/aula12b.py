num = int(input('Digite um número inteiro: '))
print('\033[4;33;46m----------\nCONVERSOR\n----------\033[m')
print('[1] converter para BINÁRIO')
print('[2] converter para OCTAL')
print('[3] converter para HEXADECIMAL')
opcao = int(input('Escolha uma das bases para conversão: '))
print('Sua opção: ',opcao)

while opcao < 1 or opcao > 3:
    opcao = int(input('Sua opção: '))
if opcao == 1:
    bin = str(bin(num))
    print(f'{num} convertido para BINÁRIO é igual a {bin[2:]}')
elif opcao == 2:
    oct = str(oct(num))
    print(f'{num} convertido para OCTAL é igual a {oct[2:]}')
elif opcao == 3:
    hexa = str(hex(num))
    print(f'{num} convertido para HEXADECIMAL é igual a {hexa[2:]}')
else:
    opcao = int(input("Sua opção"))    