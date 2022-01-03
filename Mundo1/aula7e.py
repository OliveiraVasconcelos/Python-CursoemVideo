###escreva um programa que receba um numero em metros e, converta para centimetros e milimetros
#para converte de metros para cm basta multiplicar o valor recebido por 100
#para converte de metros para cm basta multiplicar o valor recebido por 100
metros = float(input('Digite a quantidade em metros: '))
m_para_cm = metros * 100
m_para_mlm = metros * 1000
print('{}m convertido em cm fica {}cm, e convertido em mlm fica {}mlm'.format(metros, m_para_cm, m_para_mlm))