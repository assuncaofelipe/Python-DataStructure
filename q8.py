# -*-conding: utf-8 -*-
#!python3

# Escreva algoritmo que leia um vetor de 100 elementos. 
# O programa deve informar a quantidade de números ímpares existentes no vetor.
# Valores informados ou gerados pelo computador;
# #

n = 5
cout = 0
vet = [0]*n

print (vet)

for i in range(n):
    #print('Valor para a posição: ', i)
    vet[i] = int(input('Digite um valor: '))
    if vet[i] % 2 == 1:
#        print('ímpar encontrado')
        cout += 1

print(vet)
print('Número impares encontrados: ', cout, )