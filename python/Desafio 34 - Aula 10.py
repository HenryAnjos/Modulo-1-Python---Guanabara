#Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. 
#Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.

#Input do salario do Usuario 
salario = int(input('Digite o Valor do seu Salario: '))

#se o salario for maior que 1250,...
if salario > 1250.00:
    #calculo pro aumento de 10% do salario
    aumento = salario * (0.1)
    #calculo de quanto vai ficar o novo salario 
    novo_salario = aumento + salario 
    print(f'PARABENS! Voce recebeu um aumento e seu salario passara a ser {novo_salario:.2f}')
    
#qualquer outro valor abaixo de 1250,...
else:
    #calculo pro aumento de 15% do salario 
    aumento2 = salario*(0.15)
    #calculo de quanto vai ficar o novo salario 
    novo_salario2 = aumento2 + salario
    print(f'PARABENS! Voce recebeu um aumento e seu salario passara a ser {novo_salario2:.2f}')