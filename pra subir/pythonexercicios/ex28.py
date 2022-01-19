import random
x=random.randint(0,10)
print('vamos ver se vc é bom em adivinhação ? qual numero eu escolhi')
n=int(input('digite um numero de 0 á 10 ' ))
if n==x:
    print('parabens! vc acertou')
else:
    print('que pena não foi dessa vez o numero era {}'.format(x))