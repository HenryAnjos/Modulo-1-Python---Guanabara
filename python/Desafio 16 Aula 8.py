#Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira

import math 
numero= float(input('Digite um numero:'))

#deixa o numero inteiro
print(f'{math.trunc(numero)}')