from colorama import Fore, Style, init

init(autoreset=True)


def somar(a, b):
    return a + b


def multiplicar(a, b):
    return a * b


def dividir(a, b):
    return a / b


def tabuada(n):
    for t in range(1, 11):
        print(f'{n} x {t} = {n * t}')


def menu():
    print(Fore.CYAN + 4 * '==*==')
    print(Style.BRIGHT + '[1] Somar')
    print(Style.BRIGHT + '[2] Multiplicar')
    print(Style.BRIGHT + '[3] Dividir')
    print(Style.BRIGHT + '[4] Tabuada')
    print(Style.BRIGHT + '[5] Sair')


def painel():
    while True:
        try:  # protege o programa de possíveis erros do usuário.
            menu()  # chama a função menu.

            opcao = int(input(Fore.CYAN + '\nEscolha uma das opções acima: '))

            if opcao == 1:
                a = int(input(Fore.CYAN + 'Digite um número: '))
                b = int(input(Fore.CYAN + 'Digite outro número: '))
                print(f'Somar = {somar(a, b)}')

            elif opcao == 2:
                a = int(input(Fore.CYAN + 'Digite um número: '))
                b = int(input(Fore.CYAN + 'Digite outro número: '))
                print(Fore.GREEN + f'Multiplicação = {multiplicar(a, b)}')

            elif opcao == 3:
                a = int(input(Fore.CYAN + 'Digite um número: '))
                b = int(input(Fore.CYAN + 'Digite outro número: '))
                resultado = dividir(a, b)
                if resultado is None:
                    print('Não é possível dividir por zero.')
                else:
                    print((Fore.GREEN + f'Divisão = {resultado}'))

            elif opcao == 4:
                n = int(input(Fore.CYAN + 'Digite um número para a tabuada: '))
                tabuada(n)

            elif opcao == 5:
                print(Fore.RED + 'Saindo do programa...')
                break

            else:
                print(Fore.RED + 'Opção inválida!')

        except ValueError:  # fecha o try.
            print(Fore.RED + 'Digite apenas números inteiros.')


painel()  # da inicio ao programa.
