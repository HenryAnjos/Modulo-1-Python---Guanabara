#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto
preço_produto = float(input('Digite o valor do produto atual:'))
desconto = int(input('Digite quanto de desconto quer dar sobre o produto:'))
calculo = preço_produto - (preço_produto*desconto/ 100)
print (f'o produto custa {preço_produto}, voce vai dar {desconto} de desconto e o produto ficara {calculo} reais')