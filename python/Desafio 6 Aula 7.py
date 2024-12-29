#Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.

import math
n1 = int(input('Digite um valor'))
#dobro
d = n1*2

#triplo
t= n1 * 3

#raiz quadrada biblioteca math
r = math.sqrt(n1)

#raiz quadrada direto 
r2 = n1 **(1/2)

# (:.2f) para formatar numero com muitos digitos. \n pra quebra de linha no print
print (f'o dobro de {n1} é {d}\n o triplo é {t}\n a raiz quadrada é {r:.2f}')