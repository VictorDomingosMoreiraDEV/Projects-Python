frase = input('digite a frase: ') 
escolhaLetra = input('digite o caractere que deseja: ')
letraA = frase.count(escolhaLetra)
primeiroC = frase.find(escolhaLetra)
ultimoC = frase.rfind(escolhaLetra)

print(letraA)
print(primeiroC)
print(ultimoC)