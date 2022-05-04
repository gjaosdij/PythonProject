print('Gerador de PA')
print('-='*8)

a1 = int(input('Primeiro termo: '))
R = int(input('Razão: '))
n = 1

while n <= 10:
    print(f'{a1}', end=' → ')
    n += 1
    a1 += R

print('FIM')