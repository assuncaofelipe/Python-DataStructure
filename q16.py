# criar uma matriz identidade de tamanho NxN, onde N é informado pelo usuário.
# Criar uma segunda matriz que é o dobro da primeira.

#   1 0 0
#   0 1 0
#   0 0 1

from typing import Match

n = int(input('Dimensão da matriz:  '))
mat1 = [0] * n

# preenche a primeira matriz
for i in range(n):
    mat1[i] = [0] * n

# preenche a segunda matriz
mat2 = [0] * n
for i in range(n):
    mat2[i] = [0] * n

# imprime a matriz 1
for i in range(n):
    mat1[i][i] = 1

# divide
for i in range(n):
    print(mat1[i][:])

# multiplica a matriz por 2
for i in range(n):
    for j in range(n):
        mat2[i][j] = mat1[i][j] * 2

print('\n')

for i in range(n):
    print(mat2[i][:])