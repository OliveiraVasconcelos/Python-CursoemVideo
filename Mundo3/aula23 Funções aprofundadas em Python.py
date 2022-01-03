def leiaint(txt):
    while True:
        try:
            n = int(input(txt))
        except (ValueError,TypeError):
            print('\033[1;31mERRO: por favor, digite um número válido.\033[m')
            continue
        else:
            return n   

def leiareal(m):
    while True:
        try:
            n = float(input(m).strip())
        except(ValueError,TypeError):
            print('\033[31mERRO: por favor, digite um número real válido.\033[m')    
            continue
        else:
            return n

num = leiaint('Digite um inteiro: ')
num2 = leiareal('Digite um real: ')
print(f'O valor inteiro digitado foi {num}, o valor real digitado foi {num2}')            
