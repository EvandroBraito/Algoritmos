maior = 0
menor = 0
for c in range(1, 6):
    peso = float(input('Peso da {}° pessoa: '.format(c)))
    if peso > maior:
        maior = peso
    elif menor == 0:
        menor = peso
    elif peso < menor:
        menor = peso
print('O maior pesp lido foi de {}Kg\n'
      'O menor peso lido foi de {}Kg'.format(maior, menor))
