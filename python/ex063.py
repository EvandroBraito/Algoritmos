print('-' * 30)
print('Sequencia de Fibonacci')
print('-' * 30)
t = int(input('Quantos termos voce quer mostrar? '))
print('~' * 30)
a = 0
b = 1
cont = 1
c = 0
while cont < t:
    if t > c:
        print('{} -> '.format(a), end='')
        c += 1
    if t > c:
        print('{} -> '.format(b), end='')
        c += 1
    else:
        cont = t
    a = a + b
    b = a + b
    cont += 1
print('Fim')
print('~' * 30)
