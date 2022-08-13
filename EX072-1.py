numeros = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

while True:
    sn = ' '
    while True:
        n = int(input('Digite um número entre 0 e 20: '))

        if 0 <= n <= 20:
            print(f'Você digitou o número {numeros[n]}.')
            break
        else:
            print('Tente novamente.', end=' ')
    while sn not in 'SN':
        sn = str(input('Deseja digitar outro número [S/N]? ')).strip().upper()
    if sn == 'N':
        break
