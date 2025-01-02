#Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
# O programa deverá escrever na tela se o usuário venceu ou perdeu.

import random
import time
print ('vou pensar em um numero de 0 a 5, tente adivinhar o numero que eu pensei...')
#função randint pra escolher um numero qualquer entre 1 e 5
numero_sortido = random.randint(1,5)
#variavel input pro numero pra adivinhar
jogador = int(input('Qual numero eu pensei?:'))

#interação com o usuario 
print('PROCESSANDO')

#faz o codigo congelar por 2 segundos 
time.sleep(2)

#se o numero sortido for igual ao numero que o usuario falou,...
if numero_sortido == jogador:
    print(f'Eu pensei no numero {numero_sortido}, parabens, você acertou!')
    print('--FIM--')
    
#se nao,...
else:
    print(f'Eu pensei no numero {numero_sortido} e voce no {jogador}, Você errou mas tenta de novo!')
    print('--FIM--')