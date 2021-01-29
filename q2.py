#coding: utf-8
#!python3
# 
#   2) Escreva um programa que leia um valor em metros e o exiba convertido em milímetros,
#   aceitar virgulas na entrada do usuário:

#   a função '.replace(',','.')' é usada para aceitar pontos e virgulas
medida = float(input('Medida em metros: ').replace(',','.'))

medida2 = medida*1000

print('Conversão: ', medida2)