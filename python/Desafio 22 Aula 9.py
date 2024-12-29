#crie um programa que leia o nome completo de uma pessoa e mostre:
# nome com todas letras maiusculas X
# nome com todas as letras em minusculo X
# quantas letras tem sem os espaços X
# quantas letras tem o primeiro nome X
nome = str(input('Digite seu nome inteiro: ')).strip()

#variavel pra criar a lista 
letra_primeiro_nome = nome.split()

#puxa a variavel seguido da palavra que eu quero na lista/ conta quantas letras tem na palavra da lista 
print (f'seu primeiro nome é : {(letra_primeiro_nome[0])}, e ele possui {len(letra_primeiro_nome[0])} letras')

#troca o nome que foi digitado com espaço e printa sem espaço
print (f'nome sem espaço:{nome.replace(" ","")}')

#deixa o nome todo em minusculo
print (f'Nome em maiusculo: {nome.upper()}')

#deixa o nome todo em maiusculo
print (f'Nome em minusculo: {nome.lower()}')

#mostra quantas letras tem ao todo sem espaço
print (f'Seu nome tem {len(nome.replace(" ",""))} Letras')
