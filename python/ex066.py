c = tot = 0
while True:

    n = int(input('Digite um numero [999 para parar]: '))

    if n == 999:
        break
    tot += n
    c += 1

print(f'Voce digitou {c} e a soma entre eles foi {tot}')
