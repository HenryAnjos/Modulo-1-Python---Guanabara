#Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.
num = int(input('Digite um numero de 0 a 9999: '))
print (f'o numero {num}')

#descobri que se eu usar o simbolo "%10" ele pega o ultimo numero, seja da divisao ou do numero inteiro
unidade = num % 10
dezena = (num//10) %10
centena = (num//100)%10
milhar = (num//1000)%10
print(f'unidade: {unidade}')
print(f'dezena: {dezena}')
print(f'centena: {centena}')
print(f'milhar: {milhar}')


