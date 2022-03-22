n = str (input('Digite o seu nome: ')).strip () #utilizar strip para eliminar espaços
nome = n.split()
print('muito prazer em te conhecer !')
print('seu primeiro nome é: {}'.format(nome[0]))
print('seu ultimo nome é: {}'.format(nome[len(nome)-1]))