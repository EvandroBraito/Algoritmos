print('-=' * 20)
print('Analizador de Triangulos')
print('-=' * 20)
print('')

seg1 = float(input('Primeiro segmento: '))
seg2 = float(input('Segundo segmento: '))
seg3 = float(input('Terceiro segmento: '))

if (seg2 - seg3) < seg1 < seg2 + seg3 and (seg1 - seg3) < seg2 < seg1 + seg3 and (seg1 - seg2) < seg3 < seg1 + seg2:
    if seg1 == seg2 and seg2 == seg3 and seg3 == seg1:
        print('Os segmentos acima PODEM FORMAR um triangulo Equilatero!')
    elif seg1 == seg2 or seg2 == seg3 or seg3 == seg1:
        print('Os segmentos acima PODEM FORMAR um triangulo Isosceles!')
    else:
        print('Os segmentos acima PODEM FORMAR um triangulo Escaleno!')
else:
    print('Os segmentos acima NAO PODEM FORMAR triangulo!')
