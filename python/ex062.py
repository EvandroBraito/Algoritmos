print('Gerador de PA')
print('=' * 20)
p = int(input('Primeiro termo: '))
r = int(input('Razão: '))
t = 0
m = 10
while m != 0:
    t += m
    for c in range(m):
        print(p, end=' -> ')
        p += r
    print('PAUSA')
    m = int(input('Quantos termos voce quer mostrar a mais? '))
print('Progressão finalizada com {} termos mostrados'.format(t))
