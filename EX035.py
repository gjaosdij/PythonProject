print('-=' *15)
print('Analisador de triângulos.')
print('-=' *15)

s1 = int(input('Segmento 1: '))
s2 = int(input('Segmento 2: '))
s3 = int(input('Segmento 3: '))

if s1 < s2 + s3 and s2 < s1 + s3 and s3 < s1 + s2:
    print('Os segmentos acima podem formar um triângulo.')
else:
    print('Os segmentos acima não podem formar um triângulo.')
