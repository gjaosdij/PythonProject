import datetime

print('''[ 1 ] Feminino
[ 2 ] Masculino''')
sexo = int(input('Informe o seu sexo: '))

if sexo == 1:
    print('Você não precisa se alistar.')

if sexo == 2:

    anonas = int(input('Ano de nascimento: '))

    anoat = datetime.date.today().year
    idade = anoat - anonas
    alime = 18 - idade
    alima = idade - 18

    if anonas > anoat:
        print('\033[1:7:31mERRO\033[m')
    else:
        print('Quem nasceu em {} tem {} anos em {}.'.format(anonas, idade, anoat))

        if idade > 100:
            print('Você tem {} anos de idade?? Comé que cê tá vivo ainda?'.format(idade))
        elif 0 <= idade < 18:
            print('Você ainda terá que se alistar em {} {}.'.format(alime, 'anos' if alime > 1 else 'ano'))
        elif 0 <= idade == 18:
            print('Você deve se alistar neste ano.')
        elif 0 <= idade > 18:
            print('Já passou da hora de se alistar.', end='')
            print('Você deveria ter feito isso há {} {}.'.format(alima, 'anos' if alima > 1 else'ano'))
        else:
            print('\033[1:7:31mERRO\033[m')
