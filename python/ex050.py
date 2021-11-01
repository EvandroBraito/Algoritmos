s = 0
cont = 0
for c in range(1, 7):
    n = int(input('{}° valor: '.format(c)))
    if n % 2 == 0:
        s += n
        cont += 1
print('Voce informou {} numeros PARES e a soma foi {}.'.format(cont, s))
