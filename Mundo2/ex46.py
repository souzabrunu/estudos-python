from random import randint
valor_aleatorio = randint(1, 10)
tentativas = 0
while True:
    chute = int(input('Qual o seu chute: '))
    tentativas += 1
    if chute < valor_aleatorio:
        print('chute baixo demais')
    elif chute > valor_aleatorio:
        print('chute alto demais')
    else:
        print('acertou.')
        break
print(f'voce acertou e {tentativas} tentativas')
