n = c = tot = 0
while n != 999:
    n = int(input('Digite um numero [999 para parar]: '))
    if n != 999:
        tot += n
        c += 1
print('Voce digitou {} e a soma entre eles foi {}'.format(c, tot))
