print('-=-'*7,'LOJA VASCONCELOS','-=-'*7)

n = float(input('Digite o valor do produto: R$'))
desconto1 = n - (n * 0.1)
desconto2 = n - (n * 0.05)
juros = n + (n * 0.20)

print('[1] Pagamento à vista no dinheiro ou cheque\n[2] Pagamento à vista no cartão\n[3] Em até 2x no cartão\n[4] 3x ou mais no cartão')
opcao = int(input('Opção: '))
if opcao == 1:
    print(f'O produto custa R$:{n:.2f} com desconto de 10% fica R$:{desconto1}')
elif opcao == 2 :
    print(f'O produto custa R$:{n:.2f} com desconto de 5% fica R$:{desconto2}')
elif opcao == 3:
    print(f'O produto custa R$:{n:.2f}. Não tem desconto')
else:
    parcelas = int(input('Número de parcelas: '))
    vlr_parcelas = n / parcelas
    parcela_com_juros = juros/parcelas
    print(f'Sua compra será parcelada em {parcelas} vezes')
    print(f'O produto custa R$:{n:.2f} com juros de 20% fica {juros:.2f}')           
    print(f'O valor das parcelas com o juros fica 10x {parcela_com_juros:.2f}')