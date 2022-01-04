n = int(input('Digite um número para calcular seu fatorial: '))
c = n
f = 1
print('Calculando {}! = '.format(n), end='')
while c > 0:
    print('{}'.format(c), end='')
    print(' . ' if c > 1 else ' = ', end='')
    c -= 1
    f *= 1
print('{}'.format(f))