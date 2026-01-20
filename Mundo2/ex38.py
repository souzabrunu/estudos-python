def lista_de_produtos():

    lista = ['Pente', 'Bolsa', 'Bola']

    while True:
        novo_produto = input('Digite um novo produto: ').capitalize()

        if not novo_produto.isalpha():
            print('Digite novamente, sem espaços e numeros!')
        elif novo_produto in lista:

            print('O produto já está na lista!')
        else:
            lista.append(novo_produto)
            break

    while True:
        remover = input('Digite um produto para remover: ')
        if not remover:
            print('O produto precisa esta na lista.')
            break
        else:
            remover in lista
            lista.remove(remover)

            print('Produto removido com sucesso!')


lista_de_produtos()
