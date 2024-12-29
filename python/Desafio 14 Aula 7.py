#Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit
g = float(input('Quantos graus esta?:'))
calculo = g*1.8+32
print (f'esta {g} graus celsius e {calculo:.1f} fahremheit')