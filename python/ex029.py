velocidade = float(input('Qual a velcidade atual do carro? '))
if velocidade > 80:
    m = (velocidade - 80) * 7
    print('MULTADO! Voce excedeu o limite permitido que é de 80Km/h \nVocê deve pagar uma multa de R${:.2f}!'.format(m))
print('Tenha um bom dia! Dirija com segurança!')
