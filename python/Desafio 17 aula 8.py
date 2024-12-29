# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.
import math
#entrada dos dados do triangulo
adjacente = int(input('Digite o valor do cateto adjacente: '))
oposto = int(input('Digite o valor do cateto oposto: '))
#variavel da conta, fiz assim pra diminuir linha (math.pow elevar o numero)
calculo = math.pow (adjacente,2) + math.pow (oposto,2)
#variavel da raiz quadrada, (math.sqrt) e puxando a variavel calculo pra que esta com o resultado da conta acima armazenado
raiz_quadrada = math.sqrt (calculo)
print (f' a hipotenusa desse triangulo é {raiz_quadrada:.2f}')