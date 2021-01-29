#!python3
# -*- coding: utf-8 -*-
#   criar vetor de 100 posições com valores entre 10 e 50
#   encontrar o maior, quantas vezes aparece e uma posição onde ele pode ser encontrado

from random import *

TAM = 100
v = [0] * TAM

for i in range(TAM):
    v[i] = randint(10, 50) # numero randomico que gera valores automaticos

print(v)
maior = max(v)
print('O maior valor é: ', maior )

vezes = 0
for i in range(TAM):
    if v[i] == maior:
        vezes = vezes + 1
        posicao = i

print('Vezes: ', vezes)
print('Encontrado no indide posicao do vetor\n')