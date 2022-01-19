par =0
n1 = int(input('digite um numero'))
n2 = int(input('digite um numero'))
n3 = int(input('digite um numero'))
n4 = int(input('digite um numero'))
lista = (n1, n2, n3, n4)
print(f'voce digitou os valores {lista}')
print(f'o numero 9 apareceu {lista.count(9)}')
if 3 in lista:
     print(f'o numero 3 apareceu na posiçao {lista.index(3)+1}')
else:
    print('o numero 3 não apareceu')
print(f'os numeros pares digitados foram ',end='')
for n in lista:
     if n %2 ==0:
      print( n , end=',')









