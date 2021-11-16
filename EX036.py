casa = float(input('Valor da casa: '))
salario = float(input('Salário do comprador: '))
anos = int(input('Quantos anos de financiamento? '))

prest = casa / (anos * 12)

print('Para pagar uma casa de R${:.2f} em {} anos, a prestação será R${:.2f}.'.format(casa, anos, prest))

if prest > 0.3 * salario:
    print('Empréstimo \033[1:31mNEGADO!')
else:
    print('Empréstimo \033[1:32mCONCEDIDO!')
