media = 0
homem = ''
velho = 0
menina = 0

for p in range(1, 7):
    print('-'*5, '{}ª PESSOA'.format(p), '-'*5)
    nome = input('Nome: ').strip().capitalize()
    idade = int(input('Idade: '))
    sexo = input('Sexo [M/F]: ').strip().upper()
    media += idade/6
    if sexo == 'M':
        if idade > velho:
            velho = idade
            homem = nome
    elif sexo == 'F':
        if idade < 20:
            menina += 1           

print('A média de idade do grupo é de \033[1m{:.1f}\033[m anos.'.format(media))
print(f'O homem mais velho do grupo tem \033[1m{velho} anos\033[m e se chama \033[1m{homem}\033[m.')
print('Ao todo tem \033[1m{}\033[m mulher{} com menos de 20 anos.'.format(menina, '' if menina == 1 else 'es'))
