maior = 0
menor = 0

for p in range(1, 6):
    peso = float(input(f'Peso da {p}ª pessoa: '))
    if p == 1:
        maior = peso
        menor = peso
    else: 
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('O maior peso foi de \033[1m{:.1f}Kg\033[m e o menor foi de \033[1m{:.1f}Kg\033[m.'.format(maior, menor))
