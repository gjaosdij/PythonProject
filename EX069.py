#Concertar ifs e plural e testar se o programa funciona

maisdezoito = homens = mulheres20 = 0

while True:
    print('-'*30)
    print('CADASTRE UMA PESSOA')
    print('-'*30)

    idade = int(input('Idade: '))
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
print(f'Ao todo temos {homens} cadastrado{'' if homens == 1 else 's'}.')
print(f'E temos {mulheres20} mulher{'' if mulher == 1 else 'es'} com menos de 20 anos.')