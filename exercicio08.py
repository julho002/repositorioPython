#Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar,
# sabendo que a decisão é sempre pelo mais barato.

produto_a = float(input('Informe o valor do produto A.:'))
produto_b = float(input('Informe o valor do produto B.:'))
produto_c = float(input('Informe o valor do produto C.:'))

produto_barato=min(produto_a,produto_b,produto_c)

print('O produto recomendado para compra é produto:R$',produto_barato,'pois é o produto mais barato!')
