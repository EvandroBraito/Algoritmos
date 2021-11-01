print('-=' * 20)
print('Analizador de Triangulos')
print('-=' * 20)
seg1 = float(input('Primeiro segmento: '))
seg2 = float(input('Segundo segmento: '))
seg3 = float(input('Terceiro segmento: '))
if (seg2 - seg3) < seg1 < seg2 + seg3 and (seg1 - seg3) < seg2 < seg1 + seg3 and (seg1 - seg2) < seg3 < seg1 + seg2:
    print('Os segmentos  acima PODEM FORMAR trinangulo!')
else:
    print('Os segmentos acima NAO PODEM FORMAR triangulo!')
