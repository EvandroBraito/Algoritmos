from datetime import datetime
atual = datetime.today().year
maior = 0
menor = 0
for c in range(1, 8):
    ano = int(input('Em que ano a {}° pessoa nasceu? '.format(c)))
    idade = atual - ano
    if idade < 18:
        menor += 1
    else:
        maior += 1
print('Ao todo tivemos {} pessoas maiores de idade\nE tambem tivemos {} pessoas menores de idade'.format(maior, menor))
