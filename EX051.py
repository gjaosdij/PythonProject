print('='*20)
print('10 TERMOS DE UMA PA')
print('='*20)

a1 = int(input('Primeiro termo: '))
r = int(input('Razão: '))

for c in range(0, 10):
    print(a1 + c * r, end=' → ') # para obter "→" basta pressionar alt 26
print('FIM')