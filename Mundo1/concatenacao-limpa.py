#concatenação mais limpa.

from colorama import Fore, init

init(autoreset=True)

n = 100
p = 15
print(f"O desconto de {Fore.YELLOW} {p}% {Fore.RESET} em R$ {Fore.BLUE} {n} {Fore.RESET} é R$ {Fore.GREEN} {n * (p / 100):.2f}")
