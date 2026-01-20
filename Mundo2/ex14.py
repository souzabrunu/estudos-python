def medir_peso_pessoas():

    peso = float(input('Digite seu peso: '))
    maior = peso
    menor = peso

    for p in range(2, 6):
        peso = float(input(f'digite o peso da pessoa {p}: '))

        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso

    print('Maior peso:', maior)
    print('Menor peso:', menor)


medir_peso_pessoas()
