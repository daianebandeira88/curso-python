v=float(input('qual a velocidade que vc esta?'))
if v<=80:
    print('muito bem , continue dentro da velocidade permitida')
else:
    l=(v-80)*7
    print('vc esta acima da velocidade permitida deverá pagar a multa R$ {:2}'.format(l))