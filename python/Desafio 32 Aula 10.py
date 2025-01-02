#Faça um programa que leia um ano qualquer e mostre se ele é bissexto.

ano = int(input('Digite o ano que voce quer saber se é bissexto:'))
if ano % 4 == 0:
    print (f'O ano {ano} é bissexto')
else:
    print (f'o ano {ano} nao é bissexto')