cinco = False

while not cinco:
    print('\033[33m=-='*10, '\033[m')
    v1 = int(input('Primeiro valor: '))
    v2 = int(input('Segundo valor: '))
    print('''\033[34m[ 1 ] Somar
[ 2 ] Multiplicar
[ 3 ] Maior
[ 4 ] Novos números
[ 5 ] Sair do programa\033[m''')
    opção = int(input('>>>>> Qual a sua opção? '))
    if opção == 1:
        print(f'{v1} + {v2} = {v1+v2}')
    elif opção == 2:
        print(f'{v1} . {v2} = {v1*v2}')
    elif opção == 3:
        if v1 > v2:
            print(f'{v1} é maior que {v2}.')
        elif v2 > v1:
            print(f'{v2} é maior que {v1}.')
        else:
            print('Nem um dois números é maior, os dois são iguais.')
    elif opção == 4:
        v1 = int(input('Primeiro valor: '))
        v2 = int(input('Segundo valor: '))
    elif opção == 5:
        cinco = True
print('Finalizando...')