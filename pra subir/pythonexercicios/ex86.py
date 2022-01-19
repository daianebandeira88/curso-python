
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

#codigo do gauanabara
matriz=[[0,0,0],[0,0,0],[0,0,0]]
for l in range(0,3):
    for c in range(0,3):
        matriz[l][c]=int(input('digite um valor para [{l} e {c}]'))
print('f-='*15)
for l in range(0,3):
    for c in range (0,3):
        print(f'[{matriz[l][c]}]', end='')
    print()