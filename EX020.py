import random

n1 = input('Primeiro aluno(a): ')
n2 = input('Segundo aluno(a):  ')
n3 = input('Terceiro aluno(a): ')
n4 = input('Quarto aluno(a): ')

li = [n1, n2, n3, n4]

random.shuffle(li)

print(f'A ordem de apresentação será:', li)
