
from colorama import Fore, init

init(autoreset=True)


def lista_produtos():
    lista = ['Secador', 'Pente', 'Escova', 'Pregadeira']

    produto = input(Fore.CYAN + 'Escolha um produto: ').strip().capitalize()

    encontrado = False

    for item in lista:
        if produto == item:
            encontrado = True
            print(Fore.GREEN + 'Produto encontrado!')
            break

    if not encontrado:
        print(Fore.RED + 'Produto não encontrado!')


lista_produtos()
