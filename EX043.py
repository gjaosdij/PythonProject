# testar os ifs
peso = float(input('Insira o peso em Kg: '))
altu = float(input('Insira a sua altura em metros: '))

imc = peso / (altu ** 2)

if imc <= 0:
    print('\033[1:7:31mErro\033[m')
elif imc > 0:
    print('O IMC dessa pessoa é de \033[34m{:.2f}\033[m.'.format(imc))
    print('Você está', end=' ')
    if 0 < imc < 18.5:
        print('\033[3:31mabaixo do peso', end='')
    elif 18.5 < imc < 25:
        print('no \033[3:32mpeso ideal', end='')
    elif 18.5 < imc < 30:
        print('com \033[3:31msobrepeso', end='')
    elif 30 < imc < 40:
        print('com \033[3:31mobesidade', end='')
    else:
        print('com \033[3:31mobesidade mórbida', end='')
    print('\033[m.')
