somaidade = 0
maioridadehomem = 0
nomevelho = ''
totmulher20 = 0

for p in range(1, 5):
    print(f'----- {p}ª PESSOA -----')
    nome = input('Nome: ')
    idade = int(input('Idade: '))
    sexo = input('Sexo [F/M]: ')
    somaidade += idade
    if p == 1 and sexo in 'Mm':
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        totmulher20 += 1
mediaidade = somaidade/4
print('A média de idade do grupo é de {:.1f} anos.'.format(mediaidade))
print(f'O homem mais velho tem {maioridadehomem} anos e se chama {nomevelho}.')
print('Ao todo há {} mulher{} com menos de 20 anos.'.format(totmulher20, '' if totmulher20== 1 else 'es'))
