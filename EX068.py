#Sistema de par e ímpar não funcional, o jogo apenas aceita vitória em quando a soma é par 

import random
print('-='*15)
print('Vamos jogar par ou ímpar.')
print('-='*15)

perdeu = vitorias = 0

while not perdeu:
    escolha = str(input('Par ou ímpar [P/I]? ')).strip()
    jogada = int(input('Digite um valor: '))
    computador = random.randint
    if (jogada + computador) % 2 == 0:
        print('Você venceu!\nVamos jogar novamente...')
        vitorias += 1
    else:
        print('Você PERDEU!!!')
        break
print('-='*20)
print('Game over! Você venceu {} vezes.')
