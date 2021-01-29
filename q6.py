#coding: utf-8
#!python3
 
# 6) Calcule o tempo de uma viagem de carro. Pergunte a distância a percorrer e a
# velocidade média esperada para a viagem:

distancia = float(input('Distancia:   '))
v_media = float(input('Velocidade media:   '))

tempo = distancia / v_media

min = (round(tempo % 1, 2))
min = (min * 60)

print('O tempo é de {:.0f} horas e {:.0f} minutos'.format(tempo, min))