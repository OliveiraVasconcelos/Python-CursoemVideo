from time import sleep
def maior(v):
    if v == 1:
        print(f'Apenas {len(v)} valor foi analisado.')
        print(f'O maior foi {max(v)}')
    lista=[]
    print('ANALISANDO OS VALORES PASSADOS...')
    for i in v:
        print(i,end=' ')
        sleep(0.5)
    print(f'Foram informados {len(v)} valores ao todo')
    print(f'O maior valor informado foi {max(v)}')
    print('-='*25)


print('-='*25)
vetor = [2,9,4,5,7,1]
maior(vetor)
vetor = [4,7,0]
maior(vetor)
vetor = [1,2]
maior(vetor)
vetor = [6]
maior(vetor)
