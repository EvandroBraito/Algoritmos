fat = int(input('Digite um numero paraa\n'
                'calcular seu fatorial: '))
tot = fat
print('Calculando {}! = '.format(fat), end='')
while fat > 0:
    if fat > 1:
        print('{} x '.format(fat), end='')
    else:
        print('{} = {}'.format(fat, tot))
    fat -= 1
    tot *= fat
