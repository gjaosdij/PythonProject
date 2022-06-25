from random import randint
print('-='*15)
print('Vamos jogar par ou ímpar.')
print('-='*15)

perdeu = vitorias = 0

while True:
    escolha = ' '
    while escolha not in 'PI':
        escolha = str(input('Par ou ímpar [P/I]? ')).strip().upper()
    jogada = int(input('Digite um valor: '))
    computador = randint(0, 11)
    total = jogada + computador
    print('-'*30)
    print(f'Você jogou {jogada} e o computador {computador}, totalizando em {total}.', end=' ')
    print('Deu par.' if total % 2 == 0 else 'Deu ímpar.', end=' ')
    print('Você escolheu {}.'.format('par' if escolha == 'P' else 'ímpar'))
    
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
