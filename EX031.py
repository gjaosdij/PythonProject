print('Qual a distância de viagem em Km?')

viagem = float(input())

if 0 < viagem <= 200:
    preço1 = viagem * (1/2)
    print('O preço da viagem é R${:.2f}.'.format(preço1))

if viagem < 0:
    print('É o quê? Confira os dados novamente.')

if viagem > 200:
    preço2 = viagem * 0.45
    print('O preço total da viagem é de R${:.2f}.'.format(preço2))
