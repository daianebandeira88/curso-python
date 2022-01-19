soma=spar=acol=0
matriz=[[' ' ,' ' , ' '],[ ' ', ' ',' '],[' ',' ',' ']]
for lin in range(len(matriz)):
    for col in range(len(matriz[lin])):
        matriz[lin][col]=int(input(f'digite um numero para '))
for lin in range(len(matriz)):
    for col in range(len(matriz[lin])):
        print('|',end='\t')
        print(matriz[lin][col],end='\t')
    print('|')


    if matriz[lin][col] % 2 == 0:
        spar+=matriz[lin][col]
print('_'*62)
print('-'*62)
print(f' a soma de todos os pares é {spar}')
print(f'a soma dos valores da terceira coluna é :{matriz[0][2]+matriz[1][2]+matriz[2][2]}')
print(f'o maior numero da segunda linha é :{max(matriz[1])}')


