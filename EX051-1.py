print('='*20)
print('10 TERMOS DE UMA PA')
print('='*20)

a1 = int(input('Primeiro termo: '))
R = int(input('Razão: '))

a10 = a1 + 9 * R

for c in range(a1, a10, R):
    print(c, end=' → ')
print('FIM')