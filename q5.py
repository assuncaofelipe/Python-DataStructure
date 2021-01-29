#coding: utf-8
#!python3

# 5) Solicite o preço de uma mercadoria e o percentual de desconto. Exiba o valor do desconto 
# e o preço a pagar: 

p_produto = float(input('Valor produto:   '))
p_desconto = float(input('Percentual de desconto:     '))


p_produto_atual = p_produto - (p_produto*p_desconto/100)

print('Preço atual: ', p_produto_atual)