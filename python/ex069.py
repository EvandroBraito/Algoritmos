maior = homem = mulher = 0
while True:
    print('-' * 30)
    print('    CADASTRE UMA PESSOA')
    print('-' * 30)
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F]')).upper().strip()[0]
    if sexo == 'M':
        homem += 1
    elif sexo == 'F' and idade <= 20:
        mulher += 1
    elif idade >= 18:
        maior += 1
    escolha = ' '
    while escolha not in 'NS':
        escolha = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if escolha == 'N':
        break
print(f'Total de pessoas com mais de 18 anos: {maior}\n'
      f'Ao todo temos {homem} homem cadastrados\n'
      f'E temos {mulher} mulher com menos de 20 anos')
