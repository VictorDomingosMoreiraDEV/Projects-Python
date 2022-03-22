import math
cateto1 = int(input('Digite o valor do primeiro cateto: '))
cateto2 = int(input('Digite o valor do segundo cateto: '))
cat1 = cateto1 ** 2
cat2 = cateto2 ** 2
soma = cat1 + cat2
hip = math.sqrt(soma)
print('o valor da hipotenusa desse valor é: {:.5}'.format(hip))
