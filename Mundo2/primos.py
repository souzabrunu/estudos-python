def verificar_primo():
    n = int(input("Digite um número: "))

    if n <= 1:
        print("Não é primo")
        return

    eh_primo = True

    for i in range(2, n):
        if n % i == 0:
            eh_primo = False
            break

    if eh_primo:
        print("É primo")
    else:
        print("Não é primo")


verificar_primo()
