from random import randint
cpu = randint(0, 10)
tent = 0
play = int(input('Sou seu computador...\n'
                 'Acabei de pensar em um numero entre 0 e 10.\n'
                 'Será que voce consegue adivinhar qual foi?\n'
                 'Qual é o seu palpite? '))
if cpu == play:
    print('parabens voce ganhou')
else:
    while cpu != play:
        if cpu < play:
            play = int(input('Menos... Tente mais uma vez.\n'
                             'Qual é o seu palpite? '))
            tent += 1
        else:
            play = int(input('Mais... Tente mais uma vez.\n'
                             'Qual é o seu palpite? '))
            tent += 1
    print('Acertou com {} tentativas. Parabens'.format(tent))
