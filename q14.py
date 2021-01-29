#!python3
# -*- coding: utf-8 -*-
#   criar vetor de 100 posições com valores entre 10 e 50
#   encontrar o maior, quantas vezes aparece e uma posição onde ele pode ser encontrado
 
# usando função nativa

from random import randint

def criaVetor (tam, valorMin, valorMax):
    vetor=[0]*tam
    for i in range(tam):
        vetor[i] = randint(valorMin, valorMax)
    return vetor

vetor = criaVetor(10, 10, 50)

print('Vetor: ', vetor)

maior = max(vetor)

print('Maior: ', maior) 
print('Vezes do maior valor: ', vetor.count(maior))
print('Posicao do index do maior valor: ', vetor.index(maior))
