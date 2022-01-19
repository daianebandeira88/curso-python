s=float(input('qual o valor do seu salario'))
if s <= 1250.00  :
    a=(s*15)/100
    print('seu novo salario é {:2}'.format(s+a))
if s > 1250.00:
    a=(s*10)/100
    print('seu novo salario é {:2}'.format(s+a))