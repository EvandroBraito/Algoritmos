numero = int(input('Digite um numero inteiro: '))
print('''Escolha uma das bases para conversão:'
[1] converter para BINARIO'
[2] converter para OCTAL'
[3] converter \para HEXADECIMAL''')
escolha = int(input('Sua opção: '))
if escolha == 1:
    print('{} convertido para  Binario é igual a {}'.format(numero, bin(numero)[2:]))
elif escolha == 2:
    print('{} convertido para Octal é igual a {}'.format(numero, oct(numero)[2:]))
elif escolha == 3:
    print('{} convertido para Hexadecimal é igual a {}'.format(numero, hex(numero)[2:]))
else:
    print('ERRO! Voce deve escolher um numero entre 1 a 3!')
