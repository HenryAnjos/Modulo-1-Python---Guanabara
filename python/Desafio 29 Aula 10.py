#Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. 
# A multa vai custar R$7,00 por cada Km acima do limite.

#input da velocidade do carro do usuario
velocidade = int(input('Qual é a Velocidade Atual do Carro?:'))

#se tiver a 80 ou menos,...
if velocidade <=80:
    print(f' A velocidade da via é de 80km/h e você esta a {velocidade}km/h, Continue dirigindo com cuidado e tenha um bom dia!')
    
#se estiver a mais que 80,...
else:
    #pega a diferença entre o valor do usuario menos o valor da via, e multiplica por 7
    calculo = (velocidade - 80)*7
    print(f'MULTADO, Você esta andando acima do limite da via que é de 80km/h. Multado em R${calculo:.2f}!')