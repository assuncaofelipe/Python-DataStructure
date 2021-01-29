#
#  

soma = 0

n = int(input('Valor:   '))
while n == 0 or n < 0:
    n = int(input('Valor:   '))

for i in range(1, n+1, 1):
    print(i * 2)
    soma += (i*2)

print ('Soma: ', soma)

