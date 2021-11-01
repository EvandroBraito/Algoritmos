pessoa = ''
while pessoa != 'F' and pessoa != 'M':
    pessoa = str(input('Informe o sexo [F/M]: ')).strip().upper()[0]
    if pessoa != 'F' and pessoa != 'M':
        print('Valor invalido, informe novamente!')
        print('-' * 20)
print('Informação cadastrada! Fim')
