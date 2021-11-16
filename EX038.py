n1 = float(input('Digite um número: '))
n2 = float(input('Digite outro número: '))

if n1 > n2:
    print('O \033[32mprimeiro\033[m valor é maior.')
elif n2 > n1:
    print('O \033[32msegundo\033[m valor é maior.')
else:
    print('Os dois valores são \033[32miguais\033[m.')
