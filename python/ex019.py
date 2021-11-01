#import random

n1 = str(input('primeiro aluno: '))
n2 = str(input('Segundo aluno: '))
n3 = str(input('Terceiro aluno: '))
n4 = str(input('Quarto aluno: '))
from random import choice
sorteio = [n1, n2, n3, n4]
print('O aluno escolhido foi {}'.format(choice(sorteio)))

