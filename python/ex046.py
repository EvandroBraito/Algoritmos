# faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artificio, inicio de 10 ate 0
# , com uma pausa de 1 segundo entre eles.

from time import sleep
print('Contagem regressiva para o novo ano vai começãr!')
for c in range(10, -1, -1):
    sleep(1)
    print(c)
print('Feliz ano novooooooooooo \o/')
