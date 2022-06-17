numero = soma = 0

while True:
    numero = int(input('Digite um valor (999 para parar): '))
    if numero == 999:
        break
    soma += numero
print(f'A soma dos valores foi {soma}.')