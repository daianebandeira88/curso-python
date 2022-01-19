pt=int(input('digite o termo da PA'))
ra=int(input('digite a razão da PA'))
n=int(input('quantos termos exibir?'))
ul=pt+(n-1)*ra
ul=ul+1
for c in range(pt,ul,ra):

    print(c)