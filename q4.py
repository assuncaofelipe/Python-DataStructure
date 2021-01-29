#coding: utf-8
#!python3

#   4) Faça um programa que calcule o aumento de um salário. Ele deve solicitar o valor do salário
#   e a porcentagem do aumento. Exiba o valor do aumento e do novo salário:

salario = float(input('Salário:     ').replace(',','.'))
aumento = float(input('Porcentagem de aumento:  ').replace(',','.'))

s_atual = salario + (( salario * aumento)/100)

print('Atualizado:  ',  s_atual)