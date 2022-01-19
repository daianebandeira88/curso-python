p=float(input('digite seu peso'))
a=float(input('digite sua altura'))
imc=p/(a**2)
if imc< 18.5:
    print('vc esta abaixo do peso seu imc é {:.1f}'.format(imc))
elif imc >= 18.5 and  imc < 25.0:
    print('vc esta no peso ideal seu imc é {:.1f}'.format(imc))
elif imc >= 25.0 and imc < 30.0:
    print('vc esta com sobrepeso seu imc é {:.1f}'.format(imc))
elif imc >= 30.0 and imc < 40.0:
    print('vc esta com obesidade seu imc é {:.1f}'.format(imc))
else:
    print('vc esta com obesidade morbida seu imc é {:.1f}'.format(imc))
