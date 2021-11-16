print('Calcularemos aproximadamente a área da parede que precisa ser pintada e a quantidade de tinta necessária.')
print()

L = float(input('Largura da parede em metros: '))
h = float(input('Altura da parede em metros: '))

print('A área da parede é {:.3f}m², portanto são necessários {:.3f}L de tinta.'.format(L*h, (L*h)/2))
