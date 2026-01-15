def tabuada():
    n = int(input('Digite um numero: '))

    for t in range(1, 11,):
        resultado = n * t

        print(f'A tabuada de {n} X {t} é {resultado}')


tabuada()
