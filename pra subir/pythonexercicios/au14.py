n=1
par = impar = 0
while  n !=0:
    n = int(input('digite um numero'))
    if n !=0:
       if n % 2 ==0:
        par +=1
       else:
        impar += 1
print('vc digitou {} numeros pares e {} impares'.format(par , impar))