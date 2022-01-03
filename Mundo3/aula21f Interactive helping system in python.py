from time import sleep
def ajuda(c):
    print('\033[7;100;97m')
    help(f'{c}')
    print('\033[7;100;97m')
    print('\033[m')

def titulo1():
    x = 'SISTEMA DE AJUDA PyHELP'
    lenX = len(x)+4
    print('\033[1;97;42m~'*lenX)
    print(f'\033[1;97;42m{x:^27}',flush=False)
    print('\033[1;97;42m~\033[m'*lenX)


def titulo2(c,len):
   print('\033[1;31;107m~'*len,flush=False)
   print(f'\033[1;31;107m  Acessando o manual do comando "{c}" ')
   print('\033[1;31;107m~'*len) 


while True:
    titulo1()
    comando = str(input('\033[33mFunção ou Biblioteca >')).lower()
    msg = f"Acessando o manual do comando '{comando}'"
    lenMsg = len(msg)+4
    sleep(0.7)
    if comando == 'fim':
        print('\033[1;97;41m       FIM!')
        break
    titulo2(comando,lenMsg)
    sleep(0.7)
    ajuda(comando)



    