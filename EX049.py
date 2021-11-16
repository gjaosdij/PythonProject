numero = int(input('Digite o número que deseja ver a tabuada: '))

print('-' * 14)
for c in range(0, 11):
    print('{} . {:2} = {}'.format(numero, c, c * numero))
print('-' * 10)
