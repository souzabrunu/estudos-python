def lista_de_produtos():
    produtos = ['Shampoo', 'Condicionador', 'Máscara', 'Creme de pentear']

    while True:  # lopp para adicionar produto.
        novo_produto = input('Digite o novo produto: ').capitalize()
        if not novo_produto.isalpha():
            print('Produto inválido, use apenas letras!')
        elif novo_produto in produtos:
            print('Esse produto já existe, favor digitar um novo!')
        else:
            produtos.append(novo_produto)
            break

    while True:
        remover = input('Digite o produto que irá remover: ').capitalize()
        if remover in produtos:
            produtos.remove(remover)
            break
        else:
            print('O produto não existe!')

    print('A lista de produtos atualiazda é:', produtos)


lista_de_produtos()
