cont = int(input('Digite um numero: '))
primo = 0
for c in range(1, cont + 1):
    if cont % c == 0:
        print('\033[33m{}'.format(c), end=' ')
        primo += 1
    else:
        print('\033[31m{}'.format(c), end=' ')
print('\n\033[mO numero {} foi divisivel {} vezes'.format(cont, primo))
if primo == 2:
    print('E por isso ele É PRIMO')
else:
    print('E por isso ele NÃO É PRIMO')
