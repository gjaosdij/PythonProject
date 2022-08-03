#Consertar o programa q ta qbrado pa caraio

from this import d


print('='*40)
print('{: ^40}'.format('BANCO CEV'))
print('='*40)

valor = float(input('Que valor você quer sacar? R$'))

total = valor
céd = 50
totcéd = 0

while True:
    if total >= céd:
        total -= céd
        totcéd += 1
    else:
        if totcéd > 0:
            print(f'Total de {totcéd} cédulas de R${céd:.2f}')
        if céd == 50:
            céd = 20
        elif céd == 20:
            céd = 10
        elif céd == 10:
            céd = 1
        totcéd = 0
        if total == 0:
            break
