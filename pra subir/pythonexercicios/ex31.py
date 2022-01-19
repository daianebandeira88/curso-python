d=float(input('qual a distancia da sua viagem em km ?'))
if d<=200:
    print('a passagem vai custar {} reais'.format(d*0.50))
else:
    print('a passagem vai custar {} reais'.format(d*0.45))