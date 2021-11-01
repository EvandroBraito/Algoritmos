dis = float(input('Qual é a distancia da sua viagem? '))
print('Voce esta prestes a começar uma viagem de {:.1f}km'.format(dis))
if dis <= 200:
    dis = dis * 0.50
    print('E o precço da passsangem sera de R${:.2f}'.format(dis))
else:
    dis = dis * 0.45
    print('E o preço da sua passagem sera de R${:.2f}'.format(dis))
