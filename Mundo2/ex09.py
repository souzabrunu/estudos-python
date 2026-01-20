
def analisar_numeros():
    soma = 0
    contador = 0
    maior = None

    quantos = int(input('Quantos números você quer digitar? '))

    for i in range(quantos):
        numero = int(input('Digite um numero: '))

        soma = soma + numero
        contador = contador + 1

        if maior is None or numero > maior:
            maior = numero

    print('soma:', soma)
    print('contador:', contador)
    print('maior:', maior)


analisar_numeros()
