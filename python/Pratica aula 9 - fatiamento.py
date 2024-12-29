frase = 'curso em video python'
#fatiamento de uma letra
fatiamento = frase[6]
#fatiamento de palavra
fatiamento2 = frase[0:8]
#fatiamento do 0 ao 17
fatiamento3 = frase[:17]
#estrutura [começo:fim:quantas casa nao vai mostrar]
fatiamento4 = frase[::2]
print (f' a letra 6 da sua frase é: {fatiamento}?')
print (f' a palavra fatiada é: {fatiamento2}?')
print (f' a frase fatiada é: {fatiamento3}')
print(f'assim fica a frase pulando duas casas: {fatiamento4}')

#função pra contar quantos caracteres tem na frase 
len(frase)


#contador de caracter especifico 
count = frase.count('o')

#contador de caracter especifico com fatiamento
frase.count('o,0,13')

#encontrar palavra especifica na str
frase.find ('frase que queira encontrar')

#trocar uma plavra pela outra 
frase.replace('Python','Android')

#deixar a frase em maiusculo
frase.upper()

#deixa a frase em minusculo 
frase.lower()

#deixa somente a primeira letra da frase em maiusculo
frase.capitalize()

#deixa toda primeira letra de palavra da frase em maiusculo
frase.title()

#tira os espaços inuteis do começo e do fim da frase
frase.strip()

#tira o espaço somente da direita
frase.rstrip()

#tira o espaço somente da esquerda
frase.lstrip()

#separa as palavras da frase e coloca em lista
frase.split()
