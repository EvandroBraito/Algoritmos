v = float(input('Valor da casa: R$ '))
s = float(input('salario: R$ '))
p = int(input('prestaçao? '))
total = (v / p) / 12
print('Para pagar uma casa de R${:.2f} em {} anos a prestação será de R${:.2f}'.format(v, p, total))
if s * 30/100 <= total:
    print('Emprestimo \033[31mNEGADO\033[m!')
else:
    print('Emprestimo pode ser \033[32mCONCEDIDO\033[m!')
