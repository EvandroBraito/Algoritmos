print('-' * 30)
print('Sequencia de Fibonacci')
print('-' * 30)
t = int(input('Quantos termos voce quer mostrar? '))
print('~' * 30)
a = 0
b = 1
print('{} -> {} '.format(a, b), end='')
cont = 3
while cont <= t:
    c = a + b
    print('-> {} '.format(c), end='')
    a = b
    b = c
    cont += 1
print('-> Fim')
print('~' * 30)
