print('Analisador de triângulos: ')

r1 = float(input('Segmento 1: '))
r2 = float(input('Segmento 2: '))
r3 = float(input('Segmento 3: '))

print()

if r1 == r2 == r3 and r1 != 0 and r2 != 0 and r3 != 0:
    print('Os três segmentos são \033[3:34miguais\033[m e formam um \033[3:34mtriângulo equilátero\033[m.')
elif r1 == r2 and r3 <= r1 + r2 and r1 + r2 + r3 != 0 or r2 == r3 and r1 <= r2 + r3 and r1 + r2 + r3 != 0:
    print('\033[3:34mDois lados\033[m tem a \033[3:34mmesma medida\033[m, '
          'de maneira a formar um triângulo \033[3:34misósceles\033[m.')
elif r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os três lados são \033[3:34mdiferentes\033[m e formam um triângulo \033[3:34mescaleno\033[m.')
else:
    print('\033[1:7:31mERRO\033[m')