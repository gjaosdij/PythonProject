import datetime

anonas = int(input('Ano de nascimento: '))

anoat = datetime.date.today().year
idade = anoat - anonas

mirim = range(0, 10)
infantil = range(10, 15)
junior = range(15, 20)
senior = range(20, 26)


print('O atleta tem {} {}.'.format(idade, 'anos' if idade > 1 else 'ano'))
print('Classificação: ', end='\033[32m')

if idade < 0 or idade > 125:
    print('\033[1:7:31mERRO IDADE INVÁLIDA\033[m')
elif idade in mirim:
    print('Mirim')
elif idade in infantil:
    print('Infantil')
elif idade in junior:
    print('Júnior')
elif idade in senior:
    print('Sênior')
else:
    print('Master')
