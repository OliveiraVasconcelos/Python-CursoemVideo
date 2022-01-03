v = float(input('Qual a velocidade do carro: '))

if v > 80.0:
    print(f'Você estava à {v}Km/h, será multado!')
    valor_m = (v-80)*7
    print(f'Você será multado. A multa vai custar R$:{valor_m:.2f}')
else:
    print('Tenha um bom dia! Dirija em segurança!')    
