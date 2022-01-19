
pt=int(input('digite o primeiro termo da pa'))
ra=int(input('digite a razão da pa'))
termo= pt
cont=1
tot=0
mais=10
while mais != 0:
    tot=tot+ mais
    while cont <= tot:
         print( '{} ->'.format(termo),end='')
         termo += ra
         cont +=1
    print('pausa')
    mais=int(input('quantos termos vc quer mostrar a mais?'))
print('progressão finalizada com {} termos mostrados '.format(tot))


