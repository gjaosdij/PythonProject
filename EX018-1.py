from math import radians, sin, cos, tan

ang = int(input('Digite um ângulo: '))

sen = sin(radians(ang))
cos = cos(radians(ang))
tan = tan(radians(ang))

print('O seno de {:.2f} é {:.2f}, o cos é {:.2f} e a tangente é {:.2f}.'.format(ang, sen, cos, tan))
