import random

a1 = input('Digite o nome do aluno(a): ')
a2 = input('Digite o nome do aluno(a): ')
a3 = input('Digite o nome do aluno(a): ')
a4 = input('Digite o nome do aluno(a): ')

la = (a1, a2, a3, a4)
ra = random.choice(la)

print((f'O aluno(a) escolhido(a) foi: {ra}'))
