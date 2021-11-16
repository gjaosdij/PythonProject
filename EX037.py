numero = int(input('Digite um número inteiro: '))

print('''\033[36mEscolha uma das bases para conversão:
[ 1 ] Converter para Binário
[ 2 ] Converter para Octal
[ 3 ] Converter para Hexadecimal\033[m''')

opcao = int(input('Sua opção: '))

if opcao == 1:
    print('\033[32m{}\033[m convertido para \033[32mBinário\033[m é igual a {}.'.format(numero, bin(numero)[2:]))
elif opcao == 2:
    print('\033[32m{}\033[m convertido para \033[32mOctal\033[m é igual a {}.'.format(numero, oct(numero)[2:]))
elif opcao == 3:
    print('\033[32m{}\033[m convertido para \033[32mHexadecimal\33[m é igual a {}.'.format(numero, hex(numero)[2:]))
else:
    print('\033[1:7:31mERRO\033[m\nOpção digitada inválida, tente novamente.')
