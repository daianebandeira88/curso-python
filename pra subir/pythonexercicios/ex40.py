n1=float(input('primeira nota'))
n2=float(input('segunda nota'))
nf=(n2+n1)/2
if nf <=5.0:
    print('vc foi reprovado , sua media foi {}'.format(nf))

elif nf >= 7.0:
    print('vc foi aprovado parabens! sua media foi {}'.format(nf))
else:
    print('vc esta em recuperação sua media é {}'.format(nf))