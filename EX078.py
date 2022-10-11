listanum = []
maior = menor = 0

for c in range(0,5):
    listanum.append(int(input(f'Digite um número para a posição {c}: ')))
    if c == 0:
        maior = menor = listanum[c]
    else:
        if maior < listanum[c]:
            maior = listanum[c]
        if menor > listanum[c]:
            menor = listanum[c]
print('Você digitou os valores', listanum)
print(f'O maior valor digitado foi {maior} que aparece nas posições', end=' ')
for i, v in enumerate(listanum):
    if v == maior:
        print(f'{i}... ', end='')
print(f'\nO menor valor digitado foi {menor} que aparece nas posições', end=' ')
for i, v in enumerate(listanum):
    if v == menor:
        print(f'{i}... ', end='')
