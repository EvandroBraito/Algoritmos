massa = float(input('Qual é seu seu peso? (Kg) '))
altura = float(input('Qual é sua altura? (m) '))
imc = massa / (altura ** 2)
print('O IMC dessa pessoa é de {:.1f}'.format(imc))
if imc < 18.5:
    print('Voce esta em Abaixo do Peso')
elif imc <= 25:
    print('Voce esta em Peso ideal')
elif imc <= 30:
    print('Voce esta emSobrepeso')
elif imc <= 40:
    print('Voce esta em Obesidade')
else:
    print('Voce esta em Obesidade móbida')
