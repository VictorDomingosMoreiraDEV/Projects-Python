#forma de fatiamento de frase
from dataclasses import replace
from tkinter import N


frase = 'Curso em Video Python'
print(frase[:8]) 
print(frase[6:])
print(frase[:21:2]) #pular de 2 em 2
print(frase[::2]) #nao sei o incio e nao sei o final, mas pulo de 2 em 2

print("""\nNão tentar compreender o que viveram juntos
Chamá-los somente quando necessita deles.
É proibido não ser você mesmo diante das pessoas,
Fingir que elas não te importam\n""")

print (frase.count('o')) #fazer a contagem de caracteres = o

print(frase.upper()) #tranformar as letras em maisculo

print(frase.upper().count('O')) #juntar funçoes

print(len(frase))

print(frase.replace('Python', 'Android'))

print (len(frase.strip())) # a funçao strip remove os espaços contidos no texto

lista_dividida = frase.split() # utilizado para separar a frase em split (blocos) e selecionar a parte que voce deseja
print(lista_dividida[0])