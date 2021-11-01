print('=' * 40)
print('{:^40}'.format('10 TERMOS DE UMA PA'))
print('=' * 40)
p = int(input('Primeiro termo: '))
r = int(input('Razão: '))
for c in range(10, p, r):
    print(p, end=' -> ')

print('ACABOU')
