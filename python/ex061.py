print('Gerador de PA')
print('=' * 20)
p = int(input('Primeiro termo: '))
r = int(input('Razão: '))
c = 0
while c < 10:
    print(p, end=' -> ')
    c += 1
    p += r
print('Fim')
