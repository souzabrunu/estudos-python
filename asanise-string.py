n = str(input('Escreva seu nome completo: ')).strip()
nome = n.split() 
print('\nMuito prazer em te conhecer!\n')
print('Seu primeiro nome é {}'.format(nome[0]))
print('Seu ultimo nome é {}'.format(nome[len(nome)-1]))

