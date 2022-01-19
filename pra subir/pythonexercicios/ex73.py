times=('corinthians','inter','goias','atletico','vasco','são paulo','ceara','juventude','santos','fluminense','palmeiras','chapecoense','cruzeiro','fortaleza','ponte preta','bahia','sport','atletico mg','bragantino','gremio')
print('ESCOLHA UMA OPÇÃO \n para ver os 5 primeiros colocados [1] \n para ver os 4 ultimos colocados [2] \n para ver os times em ordem alfabetica [3] \n para saber a posiçao do chapecoense [4] ')
o=int(input('digite sua opção :'))
if o==1:
    print('os 5ª primeiros são {}'.format(times[0:5]))
elif o==2:
    print(f'os 4 ultimos colocados são {times[-4:]}')
elif o==3:
    print(sorted(times))
elif o==4:
    print('o chapecoense esta na posição',end=' ')
    print( (times.index('chapecoense')+1))