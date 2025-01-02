carro = int(input('Quantos anos seu carro tem?:'))

#se for tiver menos que 3 anos sera considerado novo
if carro <= 3:
    print ('Seu carro é novo')
    
#se tiver ente 8 e 4 anos sera considerado seminovo
elif carro <=8:
    print('Seu carro é seminovo')
    
#mais que 8 anos o carro é considerado velho
else :
    print('seu carro é velho')
    
    
print ('--Fim--')



nome = str(input('Qual é seu nome?: ')).upper().strip()
if nome == 'HENRY':
    print(f'Olá {nome}, Que bom te conheçer, que nome lindo você tem!')
else:
    print (f'Ola {nome}, que bom te conhecer!')
print('--Fim--')


n1 = float(input('Digite a nota do primeiro bimestre: '))
n2 = float(input('Digite a nota do segundo bimestre: '))
calculo = (n1+n2)/2
print (f'A sua média foi {calculo}')
if calculo <=5:
    print('Você foi reprovado')
else:
    print('Você foi aprovado')
print('--Fim---')