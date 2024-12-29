#Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo


import math 

#angulo em graus 
angulo = int(input('Quantos graus tem a circuferencia?: '))

#transformar o angulo de graus pra radianos 
angulo_radianos = math.radians(angulo)

#calculo do seno, cosseno,tangente
seno = math.sin(angulo_radianos)
cosseno = math.cos(angulo_radianos)
tangente = math.tan(angulo_radianos)

print (f'O seno é {seno:.2f}, o cosseno é {cosseno:.2f} e a tangente é {tangente:.2f}')