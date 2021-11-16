print('\033[34m''{:=^40}'.format('LOJAS GUANABARA'))
print()

preco = float(input('\033[mPreço das compras: R$'))

rsvrdit = '\033[3:32mR$'
n = '\033[m'

print()
print('''FORMAS DE PAGAMENTO
[ 1 ] À vista (dinheiro/cheque)
[ 2 ] À vista (cartão)
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')

opcao = int(input('Qual a forma de pagamento? '))

print()

if opcao <= 0 or opcao > 4 or preco <= 0:
    print('ERRO')
else:
    if opcao == 1:
        print('Sua compra de {}{:.2f}{} vai ficar por {}{:.2f}{}.'.format(rsvrdit, preco, n, rsvrdit, preco * 0.9, n))
    elif opcao == 2:
        print('Sua compra de {}{:.2f}{} vai ficar por {}{:.2f}{}.'.format(rsvrdit, preco, n, rsvrdit, preco * 0.95, n))
    elif opcao == 3:
        print('Sua compra ficará por {}{:.2f}{}.'.format(rsvrdit, preco, n))
    else:
        numpa = int(input('Quantas parcelas? '))
        preco2 = preco * 1.2
        parce = preco2 / numpa
        print('Sua compra será parcelada em \033[3:32m{}x{} '
              'de {}{:.2f}{} \033[3:31mcom juros\033[m.'.format(numpa, n, rsvrdit, parce, n))
        print('Sua compra de {}{:.2f}{} ficará por {}{:.2f}{}.'.format(rsvrdit, preco, n, rsvrdit, preco2, n))
