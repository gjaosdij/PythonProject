continuar = 's'
quantianum = soma = maior = menor = 0

while continuar in 'Ss':
    numero = int(input('Digite um número: '))
    quantianum += 1
    soma += numero
    if maior < numero:
        maior = numero
    if menor == 0 and numero > 0:
        menor = numero
    elif menor > numero:
        menor = numero
    continuar = str(input('Quer continuar [S/N]? ')).strip().lower()

media = soma/quantianum

print(f'Você digitou {quantianum} números e a média foi {media}.')
print(f'O maior valor foi {maior} e o menor foi {menor}.')