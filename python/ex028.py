from random import randint
from time import sleep
print('-=-' * 20)
print('Vou pensar em um numero entre 0 e 5. Tente adivinhar...')
print('-=-' * 20)
n = int(input('Em que numero eu pensei? '))
print('Processando...')
sleep(3)
npc = randint(0, 5)
if npc == n:
    print('Parabens! Voce conseguiu me vencer!')
else:
    print('Ganhei! Eu pensei no numero {} e nao no {}!'.format(npc, n))
