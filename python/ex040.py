n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
media = (n1 + n2) / 2
if media < 5.0:
    print('Tirando {:.1f} e {:.1f}, a média do aluno é {:.1f}\nO aluno está REPROVADO.'.format(n1, n2, media))
elif 5.0 < media < 6.9:
    print('Tirando {:.1f} e {:.1f}, a média do aluno é {:.1f}\nO aluno está RECUPERAÇÃO.'.format(n1, n2, media))
else:
    print('Tirando {:.1f} e {:.1f}, a média do aluno é {:.1f}\nO aluno está APROVADO.'.format(n1, n2, media))
