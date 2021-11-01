val = float(input('Qual é o salário do funcionário? R$'))
if val <= 1250:
    aumento = ((val * 15) / 100) + val
else:
    aumento = ((val * 10) / 100) + val
print('Quem ganhava R${:.2f} passa a ganhar R${:.2f} agora.'.format(val, aumento))
