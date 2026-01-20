def calcular_soma_media():
    soma = 0
    contador = 0

    for i in range(4):
        numero = int(input("Digite um numero: "))
        soma = soma + numero
        contador = contador + 1

    media = float(soma / contador)

    print("Soma:", soma)
    print("Quantidade:", contador)
    print("Média:", media)


calcular_soma_media()
