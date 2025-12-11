def mensagem(msg):
    tamanho = len(msg)
    print('-'*tamanho)
    print(msg)
    print('-'*tamanho)


# programa principal
mensagem('Seja bem vindo')


name = str(input('Digite seu nome: '))
print('Seu nome é {}'.format(name))
print('Obrigado por participar!')
