import math
co = float(input('Digite o valor do cateto oposto: '))
ca = float(input('Digite o valor do cateto adjascente: '))
hi = math.hypot(co, ca)
print('o valor da hipotenusa é: {:.3}'.format(hi))