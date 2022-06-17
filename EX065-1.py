numero = contador = soma = maior = menor = 0
continuar = 's'

while continuar in 'Ss':
    numero = int(input('Digite um número: '))
    contador += 1
    soma += numero
    if contador == 1:
        maior = menor = numero
    else:
        if numero > maior:
                maior = numero
        if numero < menor   :
                menor = numero
    continuar = str(input('Quer continuar [S/N]? '))

media = soma/contador

print(f'Você digitou {contador} números e a média foi {media}.')
print(f'O maior valor foi {maior} e o menor foi {menor}.')