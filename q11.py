#
# Escreva um programa em C que lê 5 valores reais, encontra o maior e o menor deles e
# mostra o resultado.

## resolução usando função interna

n = 5
vetor = [0] * n

for i in range(n):
    vetor[i] = int(input('Valor:    '))

print('\t   Maior valor: ', max(vetor))
print('\t   Menor valor: ', min(vetor))