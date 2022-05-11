print('Gerador de PA')
print('-='*8)

a1 = int(input('Primeiro termo: '))
R  = int(input('Razão da PA: '))
n = 1
total = 0
mais = 10

while mais != 0:
    total = total + mais
    while n <= total:
        print(f'{a1}', end= ' → ')
        a1 += R
        n += 1
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar a mais?'))
print(f'Progressão finalizada com {total} termos mostrados.')
