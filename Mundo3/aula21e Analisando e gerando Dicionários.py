def notas(*n,sit=False):
    """     -> Funcao para analisar notas e situacoes de varios alunos.
            :param n: uma ou mais notas dos alunos (aceita varias)
            :param sit: valor opicional indicando se deve ou nao adicionar a situacao.
            :return: um dict com varias informacoes sobre a situação da turma.
    """
    dicio={}
    maior = menor = 0
    media =0
    for i in (n):
        if i == n[0]:
            maior = i
            menor = i
            media+=i       
        else:
            if i > maior:
                maior = i
            if i < menor:
                menor = i    
            media+=i
    dicio['total'] = len(n)
    dicio['maior'] = maior
    dicio['menor'] = menor
    media = media/len(n)
    dicio['media'] = media
    if sit == True:
        if media < 5:
            dicio['situação']='RUIM'
        elif media >= 5 and media < 7:
            dicio['situação']='RAZOÁVEL'
        elif media > 7:
            dicio['situação']='BOA!'
    return dicio

#help(notas)
resp = notas(5.5, 9.5, 10, 6.5, sit=True)
print(resp)