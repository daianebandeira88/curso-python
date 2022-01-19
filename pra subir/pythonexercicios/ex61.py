
pt=int(input('digite o primeiro termo da pa'))
ra=int(input('digite a razão da pa'))
termo= pt
cont=1
while cont <= 10:
    print('{} ->'.format(termo),end='')
    termo += ra
    cont +=1

print('fim')