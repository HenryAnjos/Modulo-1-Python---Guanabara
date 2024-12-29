#Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros

n1 = float(input('Digite a metragem:'))

#conversao para centimetros
centimetros = n1*100

#conversao para milimetros
milimetros = n1*1000

#resultado
print(f'em metros é {n1}, em centimetros é {centimetros:.0f}cm e em milimetros é {milimetros:.0f}mm')