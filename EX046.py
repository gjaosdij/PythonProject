from time import sleep
import datetime

print('\033[36mOs fogos de artifício começam em...')
for c in range(10, -1, -1):
    if c % 2 == 0:
        print('\033[31m')
    else:
        print('\033[32m')
    sleep(1)
    print(c)

print('\nBUM! POW! BUM!')
print('\033[3:36mÉ ano novo!!! Agora estamos em', datetime.date.today().year + 1, end='!')