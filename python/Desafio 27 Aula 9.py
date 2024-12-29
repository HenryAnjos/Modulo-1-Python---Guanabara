#Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.
nome = str(input('Como é seu nome inteiro? '))
print (f'Prazer em te conhecer {nome}')
#.split pra deixar a str em lista
lista = nome.split()
#puxa os dados da lista, O VALOR -1 NA LISTA PUXA A ULTIMA PALAVRA 
print (f'O seu primeiro nome é {lista[0]} e seu ultimo nome é {lista[-1]} ')