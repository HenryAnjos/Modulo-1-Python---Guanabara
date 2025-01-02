primeiro_segmento = float(input('Digite o tamanho da primeira reta: '))
segundo_segmento = float(input('Digite o tamanho da segunda reta: '))
terceiro_segmento = float(input('Digite o tamanho da terceira reta: '))
if primeiro_segmento + segundo_segmento > terceiro_segmento and primeiro_segmento + terceiro_segmento > segundo_segmento and segundo_segmento + terceiro_segmento > primeiro_segmento:
    print ('É possivel fazer um triangulo com essas medidas')
else:
    print ('Não é possivel fazer um triangulo com essas medidas')