numero = int(input('Digite um número: '))
total = 0

for c in range(1, numero + 1):
    if numero % c == 0:
        print('\033[34m', end=' ')
        total += 1
    else:
        print('\033[31m', end=' ')
    print(c, end='\033[m')
print(f'\n\nO número \033[35m{numero}\033[m foi divisível \033[35m{total}\033[m vezes.')

if total == 2:
    print('E por isso ele \033[32m\033[3mé\033[m primo.')
else:
    print('Por isso ele \033[31m\033[3mnão\033[m é primo.')
