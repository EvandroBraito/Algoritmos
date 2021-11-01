print('{:+^40}'.format(' LOJAS GUANABARA '))
valor = float(float(input('Preco das compras: R$ ')))
total = valor
print('FORMAS DE PAGAMENTO\n'
      '[ 1 ] á vista dinheiro/cheque\n'
      '[ 2 ] á vista cartão\n'
      '[ 3 ] 2x no cartão\n'
      '[ 4 ] 3x ou mais no catão')
formas = int(input('Qual é a opção? '))
if formas == str:
    print('informação invalida')
elif formas > 4:
    print('informação invalida')
else:
    if formas == 1:
        total = valor - valor * 10 / 100
    elif formas == 2:
        total = valor - valor * 5 / 100
    elif formas == 3:
        total = valor
        print('Sua compra de {:.2f} sera parcelada em 2x de {:.2f}'.format(valor, valor / 2))
    elif formas == 4:
        p = int(input('Quantas parcelas? '))
        total = valor + valor * 20 / 100
        print('Sua compra sera parcelada em {}x de {:.2f} com juros'.format(p, total / p))
    print('Sua compra de {:.2f} vai custar R${:.2f} no final'.format(valor, total))