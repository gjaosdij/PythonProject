from random import randint

computador = randint(0, 10)
ntentativas = 0
print('''Sou seu computador...
Acabei de pensar em um número entre 0 e 10.
Será que você consegue advinhar qual foi?''')

jogada = int(input('Qual é o seu palpite? '))

while jogada != computador:
    if jogada < computador:
        print('Mais... Tente novamente.')
    if jogada > computador:
        print('Menos... Tente novamente.')
    ntentativas += 1
    jogada = int(input('Qual é o seu palpite? '))

print('Acertou com {} tentativa{}. Parabéns!'.format(ntentativas + 1, '' if ntentativas == 0  else 's'))