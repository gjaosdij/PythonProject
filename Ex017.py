co = float(input('Medida do cateto oposto: '))
ca = float(input('Medida do cateto adjacente:'))

hi = ((co**2) + (ca**2)) ** (1/2)

print('A hipotenusa mede {:.2f}.'.format(hi))
