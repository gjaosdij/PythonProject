print('Aluguel de carros.')

t = float(input('Número de dias que o carro foi alugado: '))
d = float(input('Distância percorrida em Km: '))

print('Preço a pagar: R${:.2f}'.format(d*0.15+t*60))
