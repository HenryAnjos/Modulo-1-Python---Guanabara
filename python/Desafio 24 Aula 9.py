#Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome “SANTO”
cidade = str(input('Onde você nasceu? ')).strip()

#aqui o print conta se da casa 0 até a 5 tem o nome santo(o variavel ta sendo jogada pra tudo minusculo pra nao ter erro)
print(cidade[:5].lower() == 'santo')