v1=int(input('digite um valor'))
v2=int(input('digite outro valor'))
op=0
while op != 5:
    print('----- escolha uma opção: -----')
    print(' SOMAR [1]\n MULTIPLICAR [2]\n MAIOR [3] \n NOVOS NUMEROS [4]\n SAIR DO PROGRAMA [5] ')
    op=int(input('>>>>> qual é a opção'))
    if op == 1:
        print('a soma dos valores é {}!'.format(v1+v2))
    if op == 2:
        print('a multiplicação dos valores é {}!'.format(v1*v2))
    if op == 3:
         if v1 > v2:
             print(' {} é o maior !'.format(v1))
         else:
             print('{} é o maior !'.format(v2))
    if op == 4:
        print('informe os numeros novamente')
        v1=int(input('primeiro valor'))
        v2=int(input('segundo valor'))
print('FIM DO PROGRAMA')