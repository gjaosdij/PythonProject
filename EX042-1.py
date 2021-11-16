print('\033[33m-='*15)
print('\033[34mAnalisador de triângulos: ')
print('\033[33m-=\033[m'*15, '\n')

tna = 'Os segmentos \033[3:31mnão podem\033[m formar um triângulo.'

r1 = float(input('Segmento 1: '))
r2 = float(input('Segmento 2: '))
r3 = float(input('Segmento 3: '))

print()

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 +r2:
    print('Os segmentos podem formar um triângulo', end=" \033[3:34m")
    if r1 == r2 == r3:
        print('equilátero', end='')
    elif r1 != r2 != r3 != r1:
        print('escaleno', end='')
    else:
        print('isósceles', end='')
    print('\033[m.')
elif r1 == 0 or r2 ==0 or r3 == 0:
    print(tna)
else:
    print(tna)
