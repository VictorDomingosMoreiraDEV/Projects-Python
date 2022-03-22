from itertools import count


frase = 'Claudia Margareth Domingos'
print(frase.upper())
print(frase.lower())

a = 'victor domingos moreira        '
a1 = a.replace(" ","")
print (len(a1.strip()))

lista_dividida = a.split()
print(len(lista_dividida[0]))