# Bug na linha 15
from time import sleep

n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
opção = 0

while opção != 5:
    print('''\033[36m[ 1 ] Somar
[ 2 ] Multiplicar
[ 3 ] Maior
[ 4 ] Novos números
[ 5 ] Sair do programa''')

    opção = int(input('\n\033[32m>>>>> Qual é a sua opção? '))
    
    if opção == 1:
        print(f'{n1} + {n2} = {n1+n2}')
    elif opção == 2:
        print(f'{n1} . {n2} = {n1*n2}')
    elif opção == 3:
        if n1 > n2:
            print(f'{n1} é maior que {n2}.')
        elif n2 > n1:
            print(f'{n2} é maior que {n1}.')
        else:
            print('Os números representam o mesmo valor, portanto nenhum é maior.')
    elif opção == 4:
        print('Informe os números novamente.')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    elif opção == 5:
        print('Finalizando', end='')
        sleep(1/2)
        print('.', end='')
        sleep(1)
        print('.', end='')
        sleep(1/2)
        print('.')
        sleep(1/2)
    else:
        print('\033[31mOpção inválida, tente novamente.\033[m')
    print('==-'*10)
print('Fim do programa. Volte sempre!')