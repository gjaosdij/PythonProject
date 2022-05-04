print('Gerador de PA')
print('-='*8)

a1 = int(input('Primeiro termo: '))
R = int(input('Razão: '))
n = 1

while n <= 10:
    print(a1 + (n - 1) * R, end=' → ')
    n += 1

print('FIM')
