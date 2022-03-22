angulo = int (input('digite o valor do angulo: '))
from math import radians, sin, cos, tan
s = sin(radians(angulo))
c = cos(radians(angulo))
t = tan(radians(angulo))
print('o valor de seno do angulo é: {:.3}\no valor do coseno do angulo é: {:.3}\no valor da tangente do angulo é: {:.3}'.format(s,c,t))
