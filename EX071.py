#Consertar o programa q ta qbrado pa caraio

print('='*40)
print('{: ^40}'.format('BANCO CEV'))
print('='*40)

valor = float(input('Que valor você quer sacar? R$'))

cinquenta = 0

while True:
    while valor % 50 == 0:
        valordiv = valor/50 
        cinquenta += 1
    if valor % 50 != 0:
        print(f'Notas de R$50.00: {cinquenta}')
        print(f'Valor restante: R${valordiv}')