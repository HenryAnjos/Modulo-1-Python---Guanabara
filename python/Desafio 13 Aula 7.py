#Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento
salario = float(input('Digite seu Salario:'))
porcentagem = int(input('Quantos porcentos de aumento voce recebeu?:'))
novo = salario + salario*porcentagem/100
print (f'Você passara a receber {novo:.2f} com {porcentagem}% de aumento ')