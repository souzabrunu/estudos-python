def calcule_valor_pago():

    valor = int(input('Digite um valor: '))

    while True:
        print('[1]- À vista dinheiro --> 10% de desconto')
        print('[2]- À vista cartão --> 5% de desconto')
        print('[3]- Em até 2x no cartão --> sem juros')
        print('[4]- 3x ou mais no cartão --> 20% de juros')

        opcao = int(input('Escolha a forma de pagamento: '))

        if opcao == 1:
            total = valor - (valor * 10 / 100)
            mensagem = "Desconto de 10% aplicado"
            break

        elif opcao == 2:
            total = valor - (valor * 5 / 100)
            mensagem = "Desconto de 5% aplicado"
            break

        elif opcao == 3:
            total = valor
            mensagem = "Pagamento em até 2x sem juros"
            break

        elif opcao == 4:
            total = valor + (valor * 20 / 100)
            mensagem = "Acréscimo de 20% aplicado"
            break

        else:
            print('Erro. Tente novamente\n')

    print(mensagem)
    print("Total a pagar: R$", total)


calcule_valor_pago()
