vc=float(input('qual o valor da casa?'))
s=float(input('qual o valor do seu salario?'))
p=int(input('qual o numero de parcelas ? '))
ps=( s *30)/100
if vc/p <= ps:
    print('seu emprestimo foi liberado')
elif vc/p>ps:
    print('seu emprestimo nao foi liberado pois exedeu 30% do seu salario')