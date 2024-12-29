#Crie um programa que leia o nome de uma pessoa e diga se ela tem “SILVA” no nome.
nome = str(input('Digite seu nome inteiro: ')).strip()

#verifica se tem silva na variavel que esta sendo jogada pra tudo minusculo
print ('seu nome tem silva?', ('silva' in nome.lower()))