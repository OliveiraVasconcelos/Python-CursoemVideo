x = float(input('Digite a distância da viagem: '))
if x <= 200:
    v_passagem = x * (0.5)
    print(f'A passagem custará R$:{v_passagem:.2f}')
else:
    v_passagem = x * (0.45)
    print(f'A passagem custará RS:{v_passagem:.2f}')    
