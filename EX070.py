total = maismil = maisbarato = 0
produtobarato = ' '

while True:
    produto = continuar = ' '
    preço = 0

    produto = str(input('Nome do produto: '))
    preço = float(input('Preço: R$'))
    
    total += preço

    if preço > 1000:
        maismil += 1
    if maisbarato == 0 or maisbarato > preço:
        maisbarato = preço
        produtobarato = produto
    
    continuar = str(input('Quer continuar [S/N]?')).strip().upper()
    
    if continuar in 'SN':
        if continuar == 'N':
            break
    else:
        print('ERROR')
print('{:-^40}'.format('FIM DO PROGRAMA'))
print(f'O total da compra foi {total:.2f}.')
print('Temos {} produto{} custando mais que R$1000.00.'.format(maismil, '' if maismil == 1 else 's'))
print(f'O produto mais barato foi {produtobarato} que custa R${maisbarato:.2f}.')
