from colorama import Fore


def tabuada():

    n = int(input('Digite um numero: '))

    for t in range(1, 11):
        resultado = t * n
        print(f' {Fore.CYAN}{t} X {n} = {Fore.GREEN}{resultado}')


tabuada()
