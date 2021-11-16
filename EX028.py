from random import randint
from time import sleep

print('-=-' * 22)
print('Vou pensar em um número de 0 a 5, será que você consegue advinhar?')
print('-=-' * 22)

aposta = int(input('Número: '))
sorteado = randint(0, 5)

print('Processando...')
sleep(1)

if aposta == sorteado:
    print('Você acertou!')

else:
    print(f'Você errou, que pena! Eu pensei no número {sorteado}. \nMais sorte na próxima vez...')
