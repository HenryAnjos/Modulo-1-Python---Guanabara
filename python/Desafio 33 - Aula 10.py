# Ler três números
n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
n3 = int(input('Digite o terceiro número: '))

# menor e o maior com o primeiro número
menor = maior = n1

# Verifica o menor número
if n2 < menor:
    menor = n2
if n3 < menor:
    menor = n3

# Verifica o maior número
if n2 > maior:
    maior = n2
if n3 > maior:
    maior = n3
print(f'Menor número: {menor}')
print(f'Maior número: {maior}')
