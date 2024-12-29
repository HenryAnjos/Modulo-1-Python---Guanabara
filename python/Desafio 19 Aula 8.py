#Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
#Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.

import random

#sorteio com numero de chamada
numero_de_alunos = int(input('Digite o numero de alunos que tem na sala:'))
sorteio = random.randint(1,numero_de_alunos)
print(sorteio)

#sorteio com nome 
nome1 = input('Digite o nome do primeiro aluno:')
nome2 = input('Digite o nome do segundo aluno:')
nome3 = input('Digite o nome do terceito aluno:')
nome4 = input('Digite o nome do quatyo aluno:')
sorteio = random.choice ([nome1,nome2,nome3,nome4])
print (f'o aluno escolhido foi o {sorteio}')
