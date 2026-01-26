from random import randint
from colorama import Fore, init

init(autoreset=True)


def jogo_de_adivinha():
    computador = randint(0, 10)
    contador = 0

    acertou = False

    while not acertou:
        numero = int(input(Fore.CYAN + 'Qual numero eu pensei? '))
        contador += 1
        if numero == computador:
            acertou = True
        else:
            if numero < computador:
                print(Fore.YELLOW + 'Mais...')
            elif numero > computador:
                print(Fore.YELLOW + 'Menos')
    print(f'Acertou com {contador} palpites')


jogo_de_adivinha()
