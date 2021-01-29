#coding: utf-8
#!python3

#   3) Escreva um programa que leia a quantidade de dias, horas, minutos e segundos do usuário. 
#   Calcule o total em segundos:

dias = int(input('Dias: '))
horas = int(input('horas: '))
minutos = int(input('minutos: '))

segundos = (minutos*60)+(horas*3600)+(dias*86400)

print('segundos:   ', segundos)