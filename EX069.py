pessoa = 0

while True:
    maisdezoito = homens = mulheres20 = 0
    sexo = ' '
    idade = -1
    pessoa += 1
    
    print('-'*30)
    print('CADASTRE UMA PESSOA')
    print('-'*30)
    print(f'PESSOA {pessoa}\n')
    
    while idade < 0:
        idade = int(input('Idade: '))
    
    while sexo not in 'MF':
        sexo = str(input('Sexo [M/F]: ')).strip().upper()

    if idade > 18:
        maisdezoito += 1
    if sexo == 'M':
        homens += 1
    if sexo == 'F' and idade < 20:
        mulheres20 += 1

    
    print('-'*30)
    continuar = str(input('Deseja continuar [S/N]? ')).strip().upper()

    if continuar == 'N':
        break
    elif continuar not in 'SN':
        print('\033[41mERROR\033[m')
print(f'Total de pessoas com mais de 18 anos: {maisdezoito}')
print('Ao todo temos {} homens cadastrado{}.'.format(homens, '' if homens == 1 else 's'))
print('E temos {} mulher{} com menos de 20 anos.'.format(mulheres20, '' if mulheres20 == 1 else 's'))
