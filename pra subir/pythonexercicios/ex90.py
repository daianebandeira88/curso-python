def matriz(m,n):
    return [[0]*n for i in range(m)]

def linhas(matriz):
    return len(matriz)

def colunas(matriz):
    return len(matriz[0])

a=[[1,0,1],[0,1,1],[1,0,1]]

atranposta=matriz(colunas(a),linhas(a))

for i in range(linhas(a)):
    for j in range(colunas(a)):
        atranposta[j][i]=a[i][j]

print(atranposta)
