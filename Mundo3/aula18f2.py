lista=[]
listaAux=[]
meida = 0
while True:
    listaAux.append(input('Nome: '))
    listaAux.append(float(input('Nota 1: ')))
    listaAux.append(float(input('Nota 2: ')))
    media = (listaAux[1] + listaAux[2])/2
    listaAux.append(media)
    lista.append(listaAux[:])
    opcao=input('Deseja continuar? [S/N]: ')
    listaAux.clear()
    media = 0
    if opcao in 'Nn':
        break
print('-='*30,'\n            BOLETIM\n','-='*30)    
print(f'No.  Nome           MÉDIA')    
print('-'*30)
for pos,i in enumerate(lista):
    print(f'{pos:^3}  {i[0]:<15} {i[3]:>3.2f} ')

aluno = int(input('Mostrar notas de qual aluno? (-1 para finalizar)'))
while aluno != -1:
        print(f'Notas de {lista[aluno][0]} são ',end='')
        print('[',lista[aluno][1],end=', ')
        print(lista[aluno][2],']')
        aluno = int(input('Mostrar notas de qual aluno? (-1 para finalizar)'))
print('   <<< FINALIZADO >>>')    