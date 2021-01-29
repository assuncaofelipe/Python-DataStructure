# criar uma matriz identidade de tamanho NxN, onde N é informado pelo usuário.
# Criar uma segunda matriz que é o dobro da primeira.

#   1 0 0
#   0 1 0
#   0 0 1

def criaMatriz (n, m):
    mat = [0]*n
    for i in range(m):
        mat[i] = [0] * n
    return mat

def criaMatrizEye(n):
    mat = criaMatriz(n,n)
    for i in range(n):
        mat[i][i] = 1
    return mat

def mostraMatriz(mat, n):
    for i in range(n):
        print(mat[i][:])
    print ('\n')

n = int(input('Tamanho matriz: '))
mat1 = criaMatrizEye(n)
mat2 = criaMatriz(n,n)

# chama as funções e imprime
mostraMatriz(mat1, n)
mostraMatriz(mat2, n)

# multiplica a matriz 1
for i in range(n):
    for j in range(n):
        mat2[i][j] = mat1[i][j] * 2
        
mostraMatriz(mat2, n)