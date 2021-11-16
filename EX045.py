from random import randint
from time import sleep

itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)

print('''\033[32mSuas opções:
[ 1 ] Pedra
[ 2 ] Papel
[ 3 ] Tesoura\033[m''')

jogador = int(input('Qual é a sua jogada? '))

jogada = jogador - 1
vencej = '\033[32mJogador vence!'
vencec = '\033[31mComputador vence!'
barra = '\033[34m-=' * 15

if jogador < 1 or jogador > 3:
    print('\033[1:7:31mERRO\033[m')
else:
    print('\033[31mJO')
    sleep(1)
    print('\033[34mKEN')
    sleep(1)
    print('\033[32mPO!')
    print(barra)
    print('\033[33mO jogador escolheu {}'.format(itens[jogada]))
    print('O computador escolheu {}'.format(itens[computador]))
    print(barra, '\033[m')
    if jogada == computador:
        print('Empate!')
    elif computador == 0:
        if jogada == 1:
            print(vencej)
        elif jogada == 2:
            print(vencec)
    elif computador == 1:
        if jogada == 0:
            print(vencec)
        elif jogada == 2:
            print(vencej)
    elif computador == 2:
        if jogada == 0:
            print(vencej)
        elif jogada == 1:
            print(vencec)
