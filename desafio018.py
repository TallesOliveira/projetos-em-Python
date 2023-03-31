from math import radians, sin, cos, tan
angulo = float(input('Digite um angulo: '))
seno = sin(radians(angulo))
coss = cos(radians(angulo))
tang = tan(radians(angulo))
print ('O angulo {}:\nEm seno vai ficar {:.2f}\nEm cosseno vai ficar {:.2f}\nEm tangente vai ficar {:.2f}'.format(angulo,seno ,coss, tang))
