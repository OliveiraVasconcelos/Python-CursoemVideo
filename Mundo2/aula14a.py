s = input('informe o seu sexo [M/F]: ')

while s not in 'MmFf':
    s = input('Dados inválidos. Por favor, informe seu sexo[M/F]: ')
if s in 'Mm':
    print('Sexo Masculino registrado com sucesso!')
elif s in 'Ff':
    print('Sexo feminino registrado com sucesso!')