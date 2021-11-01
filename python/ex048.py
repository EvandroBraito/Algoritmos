s = 0
t = 0
for c in range(3, 500, 3):
    if c % 2 == 1:
        s += c
        t += 1
print('A soma de todos os {} valores solicitados é {}'.format(t, s))
