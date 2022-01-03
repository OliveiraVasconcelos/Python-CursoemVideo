def fatorial(n,show=False):
    cont=n
    fat=1 
    while cont > 0 :
        if show == True:
            fat*=cont
            print(f'{cont} ',end='')
            if cont > 1:
                print('x',end=' ')
                cont -= 1
            else:
                print('=',end=' ')
                cont -= 1
    print(f' {fat}',end=' ')    
    print('FIM!')
    if show==False:    
        while cont > 0 :
            fat*=cont
            cont-=1
        print(fat)    


print('-'*22)
fatorial(5,show=False)      
