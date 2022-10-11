numeros = list()
n = 0

while True:
    sn = ' '
    n = int(input('Digite um valor: '))
    if n not in numeros:
        numeros.append(n)
        print('\033[32mValor adicionado a lista com sucesso.\033[m')
    elif n in numeros:
        print('\033[31mO valor já está na lista, tente outro número.\033[m')
    while sn not in 'SsNn':
        sn = str(input('Quer continuar [S/N]? '))
        if sn not in 'SsNn':
            print('\033[31mResposta inválida. A resposta deve ser S (sim) ou N (não).\033[m')
    if sn in 'Nn':
        break
print('-=-'*38)
print('Você digitou os valores', numeros)