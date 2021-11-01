tot = maior = menor = 0
nome = ''
while True:
    nome1 = str(input('Nome do produto: ')).strip()
    valor = float(input('Preço: R$'))
    tot += valor
    if menor == 0 or valor < menor:
            menor = valor
            nome = nome1
    if valor > 1000: 
        maior += 1
    resp = ' '
    while resp not in 'NS':
        resp = str(input('Quer continuar? [S/N]')).upper().strip()[0]
    if resp == 'N':
        break
print('-' * 15, 'FIM DO PROGRAMA', '-' * 15)
print(f'O total da compra foi R${tot:.2f}')
print(f'Temos {maior} produto custando mais de R$1000.00')
print(f'O produto mais barato foi {nome} que custou R${menor:.2f}')
