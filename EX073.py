#O item d pede a posição do Chapecoense, mas como não está na lista coloquei São Paulo

times = ('Palmeiras', 'Corinthians', 'Fluminense', 'Athletico-PR', 'Flamengo', 'Internacional', 'Atlético-MG', 'Bragantino', 'Santos', 'América-MG', 'São Paulo', 'Botafogo', 'Goiás', 'Ceará SC', 'Coritiba', 'Avaí', 'Fortaleza', 'Cuiabá', 'Atlético-GO', 'Juventude')

print('-='*58)
print(f'Lista de times do Brasileirão: {times}')
print('-='*58)
print(f'Os cinco primeiros são: {times[0:5]}')
print('-='*58)
print(f'Os quatro últimos são: {times[-4:]}')
print('-='*58)
print(f'Times em ordem alfabética: {sorted(times)}')
print('-='*58)
print(f'O São Paulo está na {times.index("São Paulo")+1}ª posição.')