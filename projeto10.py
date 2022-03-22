cidade = (input('digite o nome da cidade: '))
cidade1 = cidade.split()
cidade2 = (cidade1[0])
if cidade.count('Santo') == 0:
    print('A cidade {} não possui o primeiro nome como "Santo"'.format(cidade))
else:
    print('a cidade {} possui o primeiro nome como "Santo"'.format(cidade))