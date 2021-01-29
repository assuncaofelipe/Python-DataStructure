#!python3
# -*- coding: utf-8 -*-
#   criar vetor de 100 posições com valores entre 10 e 50
#   encontrar o maior, quantas vezes aparece e uma posição onde ele pode ser encontrado
 

 
# usando função nativa

from random import randint

def  encontrMaior(vetor, tam):
    maior = vetor[0]
    for i in range(1, tam):
        if vetor[i] > maior:
            maior = vetor[i]
    return maior

def criaVetor (tam, valorMin, valorMax):
    vetor=[0]*tam
    for i in range(tam):
        vetor[i] = randint(valorMin, valorMax)
    return vetor

vetor = criaVetor(100, 10, 50)
print('\n')
print('Vetor: ', vetor)

maior = encontrMaior(vetor, 100)

print('\n')
print('Maior: ', maior) 
print('Vezes do maior valor: ', vetor.count(maior))
print('Posicao do index do maior valor: ', vetor.index(maior))
print('\n')
