#Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado.
# Calcule o preço a pagar, sabendo que o carro custa R$0,15 por Km rodado

km = int(input('Quantos KM voce rodou com o carro?:'))
dias = int(input('Quantos dias voce alugou o carro?:'))
valor_da_diaria = int(input('Quanto Custou a diaria do carro?:'))
calculo1= (km*0.15) + (dias*valor_da_diaria)
print (f'voce alugou o carro por {dias} dias e rodou {km}, o total ficara em {calculo1}')