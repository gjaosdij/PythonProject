total = maismil = maisbarato = 0

while True:
    produto = continuar = ' '
    preço = 0

    produto = str(input('Nome do produto: '))
    preço = float(input('Preço: '))
    
    total += preço

    if preço > 1000:
        maismil += 1
    if maisbarato == 0 or maisbarato > preço:
        maisbarato = preço
    
    continuar = str(input('Quer continuar [S/N]?')).strip().upper()
    
    if continuar in 'SN':
        if continuar == 'N':
            break
    else:
        print('ERROR')
print(f'O total da compra foi {total}.')
print('Temos {} produto{} custando mais que R$1000.00.')
print('O produto mais barato foi {} que custa R${}.')