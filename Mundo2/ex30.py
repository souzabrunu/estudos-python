def soma_impar_multiplo():

    soma = 0
    contagem = 0

    for c in range(1, 501, 2):
        if c % 3 == 0:
            soma += c
            contagem += 1
    print(f'a soma de todos os {contagem} valores solicitados sao {soma}')


soma_impar_multiplo()
