#Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2 metros quadrados

largura = int(input('Qual a largura dessa parede?:'))
altura = int(input('Qual a altura dessa parede?:'))

#calculo pra descobrir metro quadrado
m =  largura*altura

#calculo pra descobrir quantas latas de tinta vai precisar (cada lata de tinta pinta 2 metros quadrados)
tinta = m/2


print (f' sua parede tem {m} metros quadrados e vai precisar de {tinta:.0f}L de tinta')
print ('fim')


import math
largura = int(input('Qual a largura dessa parede?:'))
altura = int(input('Qual a altura dessa parede?:'))

#cada lata pinta 2 metros quadrados
area_por_lata = 2

#calculo pra descobrir metro quadrado
calculo_metros = largura*altura

#calculo de latas necessarias
latas = math.ceil(calculo_metros/area_por_lata)

print(f'voce vai precisar de {latas}')

#mesmo codigo feito um com a biblioteca math e o outro sem a biblioteca math
