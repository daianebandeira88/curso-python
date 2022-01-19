matriz=[['','',''],['','',''],['','','']]
for lin in range(len(matriz)):
    for col in range(len(matriz[lin])):
        matriz[lin][col]=input(f'digite um numero para ')
for lin in range(len(matriz)):
    for col in range(len(matriz[lin])):
        print('|',end='\t')
        print(matriz[lin][col],end='\t')
    print('|')
print('_'*62)
