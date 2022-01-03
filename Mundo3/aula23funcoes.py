def linha(tam = 42):
    print('-'*tam)


def cabecalho(msg):
    linha()
    print(msg.center(42))
    linha() 


def menu():
    cabecalho('MENU PRINCIPAL')
    print('\033[93m1 -\033[m \033[94mVer pessoas cadastradas \033[m')
    print('\033[93m2 - \033[94mCadastrar nova pessoa \033[m')
    print('\033[93m3 - \033[94mSair do Sistema\033[m')
    linha()
    opcao()


def opcao():
    opcao = input('\033[92mSua opção: \033[m')
    while opcao not in '123':
        print('\033[91mOPÇÃO INVÁLIDA')
        opcao = input('\033[92mSua opção: \033[m')
    return opcao


#def pessoas_cadastradas()