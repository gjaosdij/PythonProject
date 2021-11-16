soma = 0
cont = 0

for c in range(1, 7):
    num = int(input('Digite o {}° valor: '.format(c)))
    if num % 2 ==0:
        soma = soma + num
        cont = cont + 1
print('''Você informou \033[1:32m{}\033[m valor{} par{} e a soma resultou em 
\033[1:32m{}\033[m.'''.format(cont, '' if cont == 1 else 'es' , '' if cont == 1 else 'es', soma))
