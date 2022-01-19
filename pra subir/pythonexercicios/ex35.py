l1=float(input('tamanho da primeira linha'))
l2=float(input('tamanho da segunda linha'))
l3=float(input('tamanho da terceira linha'))

if l1<l2 + l3 and l2 <l1+l3 and l3< l1+l2:
     print('forma um triangulo')
else:
    print('nao forma um triangulo')