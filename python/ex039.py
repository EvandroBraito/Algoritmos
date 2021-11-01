from datetime import date
sexo = str(input('Por favor, informe o seu sexo. [F] Feminino [M] Masculino: ')).lower().strip()

if sexo == 'f':
    print('Desculpe, mas penas homens sao obrigados a se alistar.')
elif sexo == 'm':
    ano = int(input('ano de nascimento: '))
    anoatual = date.today().year
    idade = anoatual - ano
    print('Quem nasceu em {} tem {} anos em {}'.format(ano, idade, anoatual))

    if idade == 18:
        print('voce deve se alistar IMEDIATAMENTE!')
    elif idade < 18:
        restante = 18 - idade
        print('Ainda faltam {} anos para o alistamento\n'
              'Seu alistamento sera em {}'.format(restante, restante + anoatual))
    else:
        restante = idade - 18
        print('Voce ja deveria ter se alistado há {}\n'
              'Seu alistamento foi em {}'.format(restante, anoatual - restante))
else:
    print('ERRO! Informação invalida.')
