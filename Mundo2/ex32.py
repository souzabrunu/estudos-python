from colorama import Fore, Style, init

init(autoreset=True)


def menu():
    print(4 * "=.=")
    print(Style.BRIGHT + "[1] add")
    print(Style.BRIGHT + "[2] multiply")
    print(Style.BRIGHT + "[3] divide")
    print(Style.BRIGHT + "[4] Exit")


def add(a, b):
    return a + b


def multiply(a, b):
    return a * b


def divide(a, b):
    return a / b


def calculate():
    while True:

        menu()
        try:
            option = int(input(Fore.CYAN + "\nChoose one of the options above.: "))

            if option == 1:
                a = int(input(Fore.CYAN + "Enter a number: "))
                b = int(input(Fore.CYAN + "Enter another number: "))
                print(Fore.GREEN + f"Add = {add(a, b)}")

            elif option == 2:
                a = int(input(Fore.CYAN + "Enter a number: "))
                b = int(input(Fore.CYAN + "Enter another number: "))
                print(Fore.GREEN + f"Multiply = {multiply(a, b)}")

            elif option == 3:
                a = int(input(Fore.CYAN + "Enter a number: "))
                b = int(input(Fore.CYAN + "Enter another number: "))
                result = divide(a, b)

                if result is None:
                    print(Fore.RED + "Cannot divide by zero.")
                else:
                    print(Fore.GREEN + f"Divide = {result:.2f}")

            elif option == 4:
                print(Fore.CYAN + "Leaving the program...")
                break
            else:
                print(Fore.RED + "Invalid option!")
        except ValueError:
            print(Fore.RED + "Enter only numbers.!")


calculate()
