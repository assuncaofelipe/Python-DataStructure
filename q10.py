#
# Escreva um programa em C que lê 5 valores reais, encontra o maior e o menor deles e
# mostra o resultado.

## resolução usando vetores
n = 7
v = [0] * n

for i in range(n):
    v[i] = int(input('Valor: '))

maior = v[0]
menor = v[0]

for i in range(0, n):
    if v[i] > maior:
        maior = v[i]
    elif v[i] < menor:
        menor = v[i]

print('\t   maior', maior)
print('\t   menor', menor)