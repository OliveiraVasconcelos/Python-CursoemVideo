expressao = str(input('Digite a sua expressão: '))
lista = []
for simb in expressao:
    if simb == '(':
        lista.append(')')
    elif simb == ')':
        if len(lista) > 0:
            lista.pop()
            break
if len(lista) == 0:
    print('Expressão válida!')
else:
    print('Esta expressão não é válida')                