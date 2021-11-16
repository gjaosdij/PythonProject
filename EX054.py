import datetime

hoje = datetime.date.today().year
maior = 0
menor = 0
viajf = 0
viajp = 0

for c in range(1, 8):
    nasc = int(input(f'Em que ano a pessoa {c}ª nasceu? '))
    if nasc + 115 <= nasc >= (hoje + 18):
        maior += 1
    elif nasc > hoje:
        viajf += 1
    elif nasc < hoje - 115:
        viajp += 1
    else:
        menor += 1
print(f'Ao todo tivemos \033[34m{maior}\033[m pessoas maiores de idade, \033[34m{menor}\033[m menores e ')
print(f'\033[34m{viajf + viajp}\033[m que não sabemos pois são viajantes do tempo.')
