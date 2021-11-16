si = float(input('Salário do funcionário: R$'))

if si < 0:
    print('ERRO! Verifique o valor informado.')
if si <= 1250:
    sa = si * 1.15
else:
    sa = si * 1.10

print('O salário de {:.2f} será corrigido para R${:.2f}.'.format(si, sa))
