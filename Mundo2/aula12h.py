peso = float(input('Digite o peso do cidadão: '))
altura = float(input('Digite a altura do cidadão: '))
imc = peso/(altura **2)

if imc < 18.5:
    print(f'IMC da pessoa é de {imc:.1f}')
    print('A pessoa está MUITO magro!')
elif imc >18.5 and imc <= 25:
    print(f'IMC da pessoa é de {imc:.1f}')
    print('Parabéns! Voçê está no peso ideal!') 
elif imc > 25 and imc <= 30:
    print(f'IMC da pessoa é de {imc:.1f}')
    print('Voçê está acima do peso ideal.') 
elif imc > 30 and imc <= 40:
    print(f'IMC da pessoa é de {imc:.1f}')    
    print('Voçê é uma pessoa obesa. CUIDADO!')
else:
    print(f'IMC da pessoa é de {imc:.1f}')
    print('Voçê está em estado de obesidade MÓRBIDA. CUIDADO!')               