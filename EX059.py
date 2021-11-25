from time import sleep
cinco = False

print('\033[33m=-='*10, '\033[m')
v1 = int(input('Primeiro valor: '))
v2 = int(input('Segundo valor: '))

while not cinco:
    print('''\033[34m[ 1 ] Somar
[ 2 ] Multiplicar
[ 3 ] Maior
[ 4 ] Novos números
[ 5 ] Sair do programa\033[m''')
    opção = int(input('>>>>> Qual a sua opção? '))
    print('\033[32m', end='')
    if opção == 1:
        print(f'{v1} + {v2} = {v1+v2}\033[m')
    elif opção == 2:
        print(f'{v1} . {v2} = {v1*v2}\033[m')
    elif opção == 3:
        if v1 > v2:
            print(f'{v1} é maior que {v2}.')
        elif v2 > v1:
            print(f'{v2} é maior que {v1}.')
        else:
            print('Nem um dois números é maior, os dois são iguais.')
    elif opção == 4:
        print('Informe os valores novamente.')
        v1 = int(input('\033[mPrimeiro valor: '))
        v2 = int(input('Segundo valor: '))
    elif opção == 5:
        cinco = True
        print('Finalizando...')
        sleep(2)
    else:
        print('Opção inválida. Tente novamente.')
    print('\033[33m=-='*10, '\033[m')
print('Fim do programa! Volte sempre!')
