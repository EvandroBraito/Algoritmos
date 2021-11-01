n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
n3 = int(input('Terceiro valor: '))
if n1 > n2 and n1 > n3:
    maior = n1
else:
   if n2 > n1 and n2 > n3:
    maior = n2
   else:
       if n3 > n1 and n3 > n2:
           maior = n3
print('maior {}'.format(maior))
if n1 < n2 and n1 < n3:
    menor = n1
else:
    if n2 < n1 and n2 < n3:
        menor = n2
    else:
        if n3 < n1 and n3 < n2:
            menor = n3
print('menor {}'.format(menor))
