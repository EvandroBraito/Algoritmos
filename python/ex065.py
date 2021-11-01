escolha = ''
dig = tot = maior = menor = 0
while escolha != 'n':
    n = int(input('Digite um numero: '))
    escolha = str(input('Quer continuar? [S/N]')).lower().strip()[0]
    if n > maior:
        maior = n
    elif menor == 0:
        menor = n
    elif n < menor:
        menor = n
    tot += n
    dig += 1
media = tot / dig
print('Voce digitou {} numeros e a media foi {:.2f}'.format(dig, media))
print('O maior valor foi {} e o menor foi {}'.format(maior, menor))
