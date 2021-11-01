from time import sleep
n1 = int(input('Primeiro valor: '))
n2 = int(input('Sugundo valor '))
opc = 0
while opc != 5:
    print('    [ 1 ] somar\n'
          '    [ 2 ] multiplicar\n'
          '    [ 3 ] maior\n'
          '    [ 4 ] novos numeros\n'
          '    [ 5 ] sair do programa')
    opc = int(input('>>>>> Qual a sua opção? '))
    if opc == 1:
        resp = n1 + n2
        print('A soma entre {} + {} é {}'.format(n1, n2, resp))
    elif opc == 2:
        resp = n1 * n2
        print('O resultado de {} x {} é {}'.format(n1, n2, resp))
    elif opc == 3:
        if n1 > n2:
            resp = n1
        else:
            resp = n2
        print('Entre {} e {} o maior é {}'.format(n1, n2, resp))

    elif opc == 4:
        print('Informe os numeros novamente: ')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Sugundo valor '))
    elif opc > 5 or opc <= 0:
        print('Opção invalida. Tente novamente')
    print('=-' * 20)
print('finalisando...')
sleep(1)
print('Fim do programa! Volte sempre!')
