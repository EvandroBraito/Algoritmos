total = 0
media = 0
maioridade = 0
nomevelho = ''
mulheres = 0
for c in range(1, 5):
    print('----- {}° Pessoa -----'.format(c))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sx = str(input('Sexo[M/F]: ')).strip().upper()
    total += idade
    media = total / 4
    if idade > maioridade:
        maioridade = idade
        nomevelho = nome
    if sx == 'F' and idade < 20:
        mulheres += 1
print('A media de idade do grupo é de {} anos\n'
      'O homem mais velho tem {} anos e se chama {}\n'
      'Ao todo são {} com menos de 20 anos'.format(media, maioridade, nomevelho, mulheres))

