###Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra “A”
# em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.

frase = str(input('Digite uma frase: ')).strip().upper()
#linha pra contar quantos A tem na frase 
contador = frase.count('A')
print (f'A palavra tem {contador} "A"')

#print do primeiro A da frase, usando o .find +1 pra nao mostrar que a primeira letra é 1 ao invés de 0 caso seja a primeira letra 
print (f'A primeira letra "A" está na posição:{frase.find('A')+1}')   

#print do ultimo A usando o .rfind que le da direita pra esquerda 
print(f'A ultima letra "A" esta na posição:{frase.rfind('A')}')    