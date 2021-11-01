from random import randint
vit = 0
while True:
    print('=-' * 15)
    print('VAMOS JOGAR PAR OU IMPAR')
    print('=-' * 15)
    n = int(input('Diga um valor: '))
    cpu = randint(0, 10)
    jogada = cpu + n
    parImpar = ' '
    while parImpar not in 'PI':
        parImpar = str(input('Par ou Impar? [P/I] ')).upper().strip()[0]
    print('-' * 30)
    print(f'Voce jogou {n} e o computador {cpu}', end='. ')
    if jogada % 2 == 0:
        compara = 'P'
        print(f'Total de {jogada} deu PAR')
    else:
        compara = 'I'
        print(f'Total de {jogada} deu IMPAR')
    print('-' * 30)
    if parImpar == compara:
        print('Voce VENCEU')
        print('Vamos jogar novamente...')
        vit += 1
    else:
        print('Voce PERDEU')
        break
print('=-' * 15)
print(f'GAME OVER! Voce venceu {vit} vezes')
