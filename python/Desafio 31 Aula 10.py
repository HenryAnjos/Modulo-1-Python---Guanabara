# Desenvolva um programa que pergunte a distância de uma viagem em Km.
# Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.

#input da distancia da viagem do usuario
distancia = int(input('Quantos kilometros tem a sua viagem: '))

#se o usuario tiver uma viagem de 200km ou menos,... 
if distancia <=200:
    #calculo pra saber o valor da passagem, input do usuario multiplica por 0,50
    calculo = distancia * 0.50
    print (f'Voce percorrera {distancia}KM, logo a sua viagem custará {calculo:.2f}')
    
#se o usuario tiver uma viagem de 200km ou mais,...
else:
    #calculo pra saber o valor da passagem de uma viagem de mais de 200km, input do usuario multiplica por 0,40
    calculo2 =distancia*0.45
    print(f'Voce percorrera{distancia}KM, logo a sua viagem custara {calculo2:.2f}')
