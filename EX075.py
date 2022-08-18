#Terminar exercício

from gettext import find


n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite mais um número: '))
n3 = int(input('Digite outro número: '))
n4 = int(input('Digite o último número: '))

numeros = (n1, n2, n3, n4)
num9 = numeros.count(9)

print('Você digitou os valores', numeros)

if num9 == 0:
    print('O número 9 não foi digitado nenhuma vez.')
elif num9 > 0:
    print(f'O numero 9 foi digitado {num9} vez{"" if num9 == 1 else "es"}.')

if 3 in numeros:
    print(f'O primeiro valor 3 foi digitado na {numeros.index(3)+1}ª posição.')
else:
    print('O valor 3 não foi digitado.')

print('Os valores pares digitados foram:', end=' ')
for n in numeros:
    if n % 2 == 0:
        print(n, end=' ')
