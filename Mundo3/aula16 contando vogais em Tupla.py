def vogal(palavra):
    lista=[]
    for letra in palavra:
        if letra in 'aeiou':
            lista.append(letra)
    return lista


tupla = ('amar','trabalhar', 'estudar',
'desenhar','matar','chamar','armonizar')


for palavra in tupla:
    lista=vogal(palavra)
    print(f'Na palavra {palavra} temos: ',end="")
    print(*lista)    
    