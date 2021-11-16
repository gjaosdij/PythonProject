n1 = float(input('Nota mensal: '))
n2 = float(input('Nota bimestral: '))

ms = (n1 + n2) / 2

print('Tirando {}{:.1f}\033[m e'.format('\033[31m' if n1 < 7 else '\033[32m', n1), end='')
print(' {}{:.1f}\033[m,'.format('\033[31m' if n2 < 7 else '\033[32m', n2), end='')
print(' a média do aluno é {}{:.1f}\033[m.'.format('\033[31m' if ms < 7 else '\033[32m', ms))

if n1 > 10 or n2 > 10 or n1 < 0 or n2 < 0:
    print('\033[1:7:31mERRO\033[m')
elif ms < 5:
    print('\033[1:31mREPROVADO!!!')
elif 5 <= ms < 7:
    print('Você está de \033[3:31mrecuperação\033[m.')
elif 7 <= ms <= 10:
    print('Você está \033[32maprovado\033[m.')
