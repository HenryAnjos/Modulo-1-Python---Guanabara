#Faça um programa que leia um número Inteiro qualquer e mostre na tela a sua tabuada.

#forma 1 (jeito q eu fiz)
n1= int(input('Digite um numero'))
multiplicação = n1*1,n1*2,n1*3,n1*4,n1*5,n1*6,n1*7,n1*8,n1*9,n1*10
print (multiplicação)

#forma 2 (guanabara)
print('-'*12)
print ('{}X{}={}'.format(n1,1,n1*1))
print ('{}X{}={}'.format (n1,2,n1*2))
print('{}X{}={}'.format(n1,3,n1*3))
print('{}X{}={}'.format(n1,4,n1*4))
print('{}X{}={}'.format(n1,5,n1*5))
print('{}X{}={}'.format(n1,6,n1*6))
print('{}X{}={}'.format(n1,7,n1*7))
print('{}X{}={}'.format(n1,8,n1*8))
print('{}X{}={}'.format(n1,9,n1*9))
print('{}X{}={}'.format(n1,10,n1*10))
print('-'*12)