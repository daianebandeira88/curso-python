matriz=[['a00','a01','a02'],['a10','a11','a12'],['a20','a21','a22']]
ele=[0,0,0]
for i in len(matriz):
    for j in len(matriz):
        if i == j:
         ele[i]=matriz[i][j]
print('diagonal')
print(ele)