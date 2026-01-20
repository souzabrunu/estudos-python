def lista_de_convidados():

    nomes = ['Bruno', 'Ricardo', 'Bia']

    while True:
        novo_convidado = input('Digite um novo nome: ').capitalize()

        if not novo_convidado.isalpha():
            print('Erro! Digite somente letras e sem espaços.')
        elif novo_convidado in nomes:
            print('O convidado já esta na lista!')
        else:
            nomes.append(novo_convidado)
            break

    while True:
        remover = input('Digite um nome para remover da lista: ').capitalize()
        if remover in nomes:
            nomes.remove(remover)
            break
        else:
            print('O convidado não existe!')
    print('A lista de convidados atualizada é', nomes)


lista_de_convidados()
