from random import randint
print('-='*15)
print('Vamos jogar par ou ímpar.')
print('-='*15)

perdeu = vitorias = 0

while True:
    escolha = str(input('Par ou ímpar [P/I]? ')).strip().upper()
    jogada = int(input('Digite um valor: '))
    computador = randint(0, 11)
    total = jogada + computador
    
    if escolha == 'P':
        if total % 2 == 0:
            print('Você venceu!\nVamos jogar novamente...')
            vitorias += 1
        else:
            print('Você PERDEU!!!')
            break
    if escolha == 'I':
        if total % 2 == 0:
            print('Você PERDEU!!!')
            break
        else:
            print('Você venceu!\nVamos jogar novamente...')
            vitorias += 1
print('-='*20)
print(f'Game over! Você venceu {vitorias} vezes.')
