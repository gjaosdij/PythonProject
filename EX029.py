print('Qual a velocidade do carro em km/h?')

vel = float(input())
mul = 7 * (vel - 80)

if vel > 80:
    print('MULTADO! Você excedeu o limite de velocidade permitido!')
    print(f'Você deve pagar uma multa de R${mul}!')

if 0 < vel < 80:
    print('No limite de velocidade.')

if vel < 0:
    print('Tá maluco!? MULTADO!!!')

print('Tenha um bom dia! Dirija com segurança.')
