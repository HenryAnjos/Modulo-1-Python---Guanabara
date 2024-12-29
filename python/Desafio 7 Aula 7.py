#Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.

n1 = float(input('Digite a nota do primeiro Tri:'))
n2 = float(input('Digite a nota do segundo Tri:'))
n3 = float(input('Digite a nota do terceiro Tri:'))
s = n1+n2+n3
media = s/3
print (f'A média do Aluno é {media}')