#coding: utf-8
#!python3

#   7) Converta uma temperatura digitada em Celsius para Fahrenheit. F = 9*C/5 + 32. 8)
#   Faça agora o contrário, de Fahrenheit para Celsius.

t_c = int(input('Temperatura em Celcius:   '))

t_F = (9*(t_c /5)+32)

print('Temperatura em F:    ', t_F)

## conversão de Fahrenheit para Celsius
# Exercicio 08
# °C = (°F − 32) / 1,8

t_F = float(input('Temperatura: '))

t_c = ((t_F-32)/1.8)

print('Celcius: {:.2f}'.format(t_c))