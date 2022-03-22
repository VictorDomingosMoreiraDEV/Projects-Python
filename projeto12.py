frase = (input('Digite a frase desejada: '))

Cont = (frase.count('a'))
Pos1 = frase.find('a')
Pos2 = frase.rfind('a')
print('a letra "a", aparece {} vezes.\na primeira posição do "a" é: {}\na ultima posição do "a" é: {}'.format(Cont, Pos1, Pos2))