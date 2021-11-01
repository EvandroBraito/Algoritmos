n = float(input('Qual é o salário do Funcionário? R$'))
print('Um funcionario que ganhava R${:.2f}, com 15% de aumento, passa a receber R${:.2f}'.format(n, n * 15 / 100 + n))
