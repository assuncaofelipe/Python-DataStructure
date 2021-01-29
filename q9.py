#
# Escreva um programa em C que lê 5 valores reais, encontra o maior e o menor deles e
# mostra o resultado.

## resolução usando comparativo
x = int(input('Numero: '))
maior = x
menor = x

for i in range (4):
    x = int(input('Numero: '))

    if x > maior:
        maior = x
    elif x < menor:
        menor = x

print('\t   Maior: ', maior)
print('\t   Menor: ', menor)