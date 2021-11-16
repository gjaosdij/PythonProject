nome = input('Digite seu nome: ').strip()

print('Analisando seu nome...')
print('Seu nome em maiúsculas é', nome.upper())
print('Seu nome em minúsculas é', nome.lower())
print('Seu nome tem ao todo {} letras'.format(len(nome) - nome.count(' ')))

quebra = nome.split()

print('Seu primeiro nome é {} e tem {} letras.'.format(quebra[0], len(quebra[0])))
