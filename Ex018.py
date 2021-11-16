import math

ang = int(input('Valor do ângulo: '))

sen = math.sin(math.radians(ang))
cos = math.cos(math.radians(ang))
tan = math.tan(math.radians(ang))

print('O seno de {} e {:.2f}, os cosseno é {:.2f} e a tangente é {:.2f}.'.format(ang, sen, cos, tan))
