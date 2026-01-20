def calcular_total():
    soma = 0
    contador = 0

    quantos = int(input('quantos números você quer digitar: '))

    for i in range(quantos):

        numero = int(input('digite um número: '))
        soma = soma + numero
        contador = contador + 1

    print('soma:', soma)
    print('quantidade:', contador)


calcular_total()
