
def estoque_de_produtos():
    lista = ['Coloracão', 'Papel', 'Pó descolorante']

    while True:
        novo_produto = input('Digite o novo produto: ').capitalize()

        if not novo_produto.isalpha():

            print('produto nao adicioando.')
        elif novo_produto in lista:

            print('produto já existe na lista.')
        else:
            lista.append(novo_produto)
            break

    while True:
        remover_produtos = input('Digite o produto a retirar:').capitalize()

        if remover_produtos in lista:
            lista.remove(remover_produtos)
            break
        else:
            print('O produto nao existe!')

    print('Produtos atualizados:', lista)


estoque_de_produtos()
