def menu():
    print(4 * '=*=')
    print('[1] Dobro')
    print('[2] Metade')
    print('[3] Par ou Ímpar')
    print('[4] Maior entre dois números')
    print('[5] Sair')


def dobro(n):
    return n * 2


def metade(n):
    return n / 2


def par_ou_impar(n):
    return n % 2 == 0


def maior(a, b):
    if a > b:
        return a
    elif b > a:
        return b
    else:
        return None


def painel():
    while True:
        try:
            menu()
            opcao = int(input('Digite uma das opções: '))

            if opcao == 1:
                n = int(input('Digite um número: '))
                print(f'Dobro = {dobro(n)}')

            elif opcao == 2:
                n = int(input('Digite um número: '))
                print(f'Metade = {metade(n)}')

            elif opcao == 3:
                n = int(input('Digite um número: '))
                if par_ou_impar(n):
                    print('Par')
                else:
                    print('Ímpar')

            elif opcao == 4:
                n = int(input('Digite um número: '))
                n2 = int(input('Digite outro número: '))
                resultado = maior(n, n2)
                if resultado is None:
                    print('Os números são iguais')
                else:
                    print(f'Maior = {resultado}')

            elif opcao == 5:
                print('Saindo...')
                break

            else:
                print('Opção inválida')

        except ValueError:
            print('Digite apenas números')


painel()
