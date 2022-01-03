def escreva(txt,l):
    print('~'*l)
    print(f' {txt:^}')
    print('~'*l)

texto = input('TEXTO: ')
l = len(texto)+2
escreva(texto,l)
texto = input('TEXTO: ')
l = len(texto)+2
escreva(texto,l)
texto = input('TEXTO: ')
l = len(texto)+2
escreva(texto,l)