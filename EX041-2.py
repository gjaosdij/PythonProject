import datetime

anonas = int(input('Ano de nascimento: '))

anoat = datetime.date.today().year
idade = anoat - anonas

print('O atleta tem {} {}.'.format(idade, 'anos' if idade > 1 else 'ano'))
print('Classificação: ', end='\033[32m')

if idade < 0 or idade > 125:
    categoria = '\033[1:7:31mERRO IDADE INVÁLIDA\033[m'
elif 0 <= idade <= 9:
    categoria = 'Mirim'
elif 9 < idade <= 14:
    categoria = 'Infantil'
elif 14 < idade <= 19:
    categoria = 'Júnior'
elif 19 < idade <= 25:
    categoria = 'Sênior'
else:
    categoria = 'Master'

print(categoria)
