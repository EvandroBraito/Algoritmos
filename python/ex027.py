nome = str(input('Digite seu nome completo: '))
print('Muito prazer em te conhecer!')
nome1 = nome.split()
U = int(len(nome1))
print('Seu primeiro nome é {}'.format(nome1[0]))
print('Seu ultimo nome é {} '.format(nome1[U - 1]))