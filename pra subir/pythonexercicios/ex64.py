
n=''
t=0
cont=0
while n != 999:
    n=int(input('digite um numero'))
    t +=n
    cont+=1
print('voce digitou {} e a some entre eles é {}'.format( cont-1,t-999))
if n == 999:
 print('fim')