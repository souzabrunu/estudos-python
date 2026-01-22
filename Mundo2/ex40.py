from colorama import Fore, Style, init

init(autoreset=True)


def lista_de_produtos():

    lista = ['Secador', 'Pente', 'Escova', 'Pregadeira']

    while True:
        print('\n--- Gerenciador de Produtos ---')
        print('1. Adicionar Novo Produto')
        print('2. Remover')
        print('3. Consultar')
        print('4. Sair')

        opcao = input('Escolha uma das opções: ').strip()

        if not opcao.isdigit():
            print(Fore.RED + 'Digite apenas números.')

            continue
        opcao = int(opcao)

        if opcao == 1:
            produto = input(Fore.CYAN + 'Digite o nome do produto a ser adicionado: ').strip().capitalize()

            if not produto.isalpha():
                print(Fore.YELLOW + 'Digite somente letras.')
            elif produto in lista:
                print(Fore.YELLOW + 'Produto já existe na lista.')
            else:
                lista.append(produto)
                print(Fore.GREEN + 'Produto adicionado com sucesso!')

        elif opcao == 2:
            remover = input(Fore.CYAN + 'Digite o produto que gostaria de remover.').strip().capitalize()

            if remover in lista:
                lista.remove(remover)
                print(Fore.GREEN + 'Produto removido com sucesso!')
            else:
                print(Fore.RED + 'Produto não está na lista. Tente novamente.')

        elif opcao == 3:
            if not lista:
                print(Fore.YELLOW + 'Lista vazia')
            else:
                print(Fore.CYAN + 'Produtos cadastrados:')
                for item in lista:
                    print(f'- {item}')

        elif opcao == 4:
            print(Fore.CYAN + 'Você saiu do programa! Até logo.')
            break
        else:
            print(Fore.CYAN + 'Digite uma opção entre 1 e 4: ')


lista_de_produtos()
