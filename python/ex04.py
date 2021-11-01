print('=' * 30)
print('Banco EBM')
print('=' * 30)
print('Limite de R$3500.')

while True:
    pedido = int(input('Qual valor voce quer sacar?  R$'))
    if pedido > 3500:
        print('Pedido acima do limete de R$3500\n'
              'Por favor! Digite novamente')
    else:
        break

tot = sed100 = sed50 = sed20 = sed10 = sed5 = sed2 = sed1 = 0

while True:
    if tot == pedido:
        break
    else:
        if tot + 100 <= pedido and sed100 < 5:
            tot += 100
            sed100 += 1
        else:
            if tot + 50 <= pedido and sed50 < 10:
                tot += 50
                sed50 += 1
            else:

                if tot + 20 <= pedido and sed20 < 25:
                    tot += 20
                    sed20 += 1
                else:
                    if tot + 10 <= pedido and sed10 < 50:
                        tot += 10
                        sed10 += 1
                    else:
                        if tot + 5 <= pedido and sed5 < 100:
                            tot += 5
                            sed5 += 1
                        else:
                            if tot + 2 <= pedido and sed2 < 250:
                                tot += 2
                                sed2 += 1
                            else:
                                if tot + 1 <= pedido and sed1 < 500:
                                    tot += 1
                                    sed1 += 1

if sed100 > 0:
    print(f'Total de {sed100} cédulas de R$100')
if sed50 > 0:
    print(f'Total de {sed50} cédulas de R$50')
if sed20 > 0:
    print(f'Total de {sed20} cédulas de R$20')
if sed10 > 0:
    print(f'Total de {sed10} cédulas de R$10')
if sed5 > 0:
    print(f'Total de {sed5} cédulas de R$5')
if sed2 > 0:
    print(f'Total de {sed2} cédulas de R$2')
if sed1 > 0:
    print(f'Total de {sed1} cédulas de R$1')

print('=' * 30)
print('Volte sempre ao BANCO EBM! Tenha um bom dia!')
