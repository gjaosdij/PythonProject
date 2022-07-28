total = maismil = maisbarato = cont = 0
produtobarato = ' '

print('-'*30)
print('{: ^30}'.format('LOJA SUPER BARATÃO'))
print('-'*30)

while True:
    produto = continuar = ' '
    preço = 0

    produto = str(input('Nome do produto: ')).strip()
    preço = float(input('Preço: R$'))
    
    total += preço
    cont += 1

    if preço > 1000:
        maismil += 1
    if cont == 1:
        maisbarato = preço
        produtobarato = produto
    else:
        if preço < maisbarato:
            maisbarato = preço
            produtobarato = produto

    while continuar not in 'SN':
        continuar = str(input('Quer continuar [S/N]? ')).strip().upper()
        if continuar not in 'SN':
            print('ERROR')
    if continuar in 'N':
        break
print('{:-^40}'.format('FIM DO PROGRAMA'))
print(f'O total da compra foi {total:.2f}.')
print('Temos {} produto{} custando mais que R$1000.00.'.format(maismil, '' if maismil == 1 else 's'))
print(f'O produto mais barato foi {produtobarato} que custa R${maisbarato:.2f}.')
