n = c = t = 0
n = int(input('Digite um número [999 para parar]: '))
while n != 999:
    c += 1
    t += n
    n = int(input('Digite um número [999 para parar]: '))
print(f'Você digitou {c} números e a soma entre eles foi {t}.')