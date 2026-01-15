def somatorio():
    soma = 0

    for s in range(0, 4):
        numero = int(input('Digite um numero: '))
        soma += numero
    print(f'A soma dos numeros foi {soma}')


somatorio()
