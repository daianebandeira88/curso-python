t=0
tot=0
import random
c=random.randint(1,5)
print('-------JOGO DA ADIVINHAÇÃO--------')
print('vamos ver se vc adivinha o numero')
while t != c:
   t=int(input('digite um numero:'))
   tot+=1
   if t == c:
     print('parabens !!! o numero era {} e vc precisou de {} tentativas'.format(t,tot))
   else:
     print('tente outra vez !')