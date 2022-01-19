from datetime import date
ano=int(input('digite o ano de nascimento'))
data=date.today()
hj=data.year
idade= hj - ano
if idade <= 9:
    print('vc tem {} anos e sua  categortia é mirim'.format(idade))
elif idade <=14:
    print('vc é da categoria infantil')
elif idade <= 19:
    print('vc é da categoria junior')
elif idade <= 25:
    print('vc é da categoria sênior')
else:
    print('vc é da categoria master')

