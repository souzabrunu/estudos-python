from colorama import Fore, Style, init

init(autoreset=True)


def lista_de_produtos():

    lista = ['Pente', 'Bolsa', 'Bola']

    while True:
        novo_produto = input(Fore.CYAN + 'Digite um novo produto: ').strip().capitalize()

        if not novo_produto.isalpha():
            print(Fore.RED + '❌ Digite novamente, sem espaços e numeros!')
        elif novo_produto in lista:

            print(Fore.YELLOW + '⚠️ O produto já está na lista!')
        else:
            lista.append(novo_produto)
            break

    while True:
        remover = input(Fore.CYAN + 'Digite um produto para remover: ').strip().capitalize()
        if remover in lista:
            lista.remove(remover)
            print()
            print(Fore.GREEN + '✅ Produto removido com sucesso!')
            break
        else:
            print(Fore.RED + '❌ O produto não está na lista. Tente novamente!')
    print()
    print(Fore.CYAN + f'📦 Lista final de produtos: {lista}\n')


lista_de_produtos()
