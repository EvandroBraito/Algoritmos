n1 = float(input('Quantos dias alugados? '))
n2 = float(input('Quantos Km rodados? '))
total = (n1 * 60) + (n2 * 0.15)
print('O total a pagar é de R${:.2f}'.format(total))
